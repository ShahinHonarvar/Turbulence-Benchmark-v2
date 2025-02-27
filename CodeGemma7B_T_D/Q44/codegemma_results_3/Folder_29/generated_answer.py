def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(52, 72):
        if nums[i] > 1 and (not is_prime(nums[i])):
            composite_nums.add(nums[i])
    return composite_nums

def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True