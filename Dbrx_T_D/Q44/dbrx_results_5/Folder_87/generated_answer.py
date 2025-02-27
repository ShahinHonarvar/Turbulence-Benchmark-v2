def composite_nums_between_indices(nums):
    if len(nums) < 52:
        return set()
    composite_nums = set()
    for i in range(43, 52):
        if i >= len(nums):
            break
        num = nums[i]
        if num > 1 and (not is_prime(num)):
            composite_nums.add(num)
    return composite_nums

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True