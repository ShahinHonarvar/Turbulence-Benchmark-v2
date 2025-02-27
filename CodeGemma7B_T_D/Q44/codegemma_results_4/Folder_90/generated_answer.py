def composite_nums_between_indices(nums):
    composites = set()
    for i in range(333, 369):
        if i < len(nums) and nums[i] != 1 and (not is_prime(nums[i])):
            composites.add(nums[i])
    return composites

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True