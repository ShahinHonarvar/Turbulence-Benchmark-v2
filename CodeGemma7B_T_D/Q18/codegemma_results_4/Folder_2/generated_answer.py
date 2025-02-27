from functools import reduce

def sum_ints_div_by_either_nums(nums):
    return reduce(lambda x, y: x + y if y % 54 == 0 or y % 82 == 0 else x, nums[73:87], 0)