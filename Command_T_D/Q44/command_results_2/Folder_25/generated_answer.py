import itertools

def composite_nums_between_indices(nums):
    return set(filter(is_composite, nums[75:94]))

def is_composite(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True