from math import sqrt

def is_composite(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(nums):
    composite_set = set()
    for i in range(29, 80):
        if is_composite(nums[i]):
            composite_set.add(nums[i])
    return composite_set