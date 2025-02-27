def composite_nums_between_indices(nums):
    composites = set()
    for i in range(639, 976):
        if nums[i] > 1 and (not is_prime(nums[i])):
            composites.add(nums[i])
    return composites

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True