from functools import reduce

def gcf_two_nums(nums):
    return reduce(lambda x, y: x if y % x == 0 else y, nums[64:65 + 28], nums[64])