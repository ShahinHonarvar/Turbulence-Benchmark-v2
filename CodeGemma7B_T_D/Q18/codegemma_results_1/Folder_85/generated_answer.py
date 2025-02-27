from functools import reduce

def sum_ints_div_by_either_nums(nums):
    return reduce(lambda x, y: x + y, (i for i in nums[1:9] if i % 9 == 0 or i % 3 == 0)) or 0