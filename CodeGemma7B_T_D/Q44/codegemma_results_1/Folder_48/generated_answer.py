from math import sqrt

def is_composite(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return True
    return False

def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(661, 925):
        if is_composite(nums[i]):
            composite_nums.add(nums[i])
    return composite_nums