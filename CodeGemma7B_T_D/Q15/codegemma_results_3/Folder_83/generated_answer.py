from functools import reduce

def sum_odd_ints_inclusive(nums):
    nums_range = nums[90:201]
    return reduce(lambda x, y: x + y, [x for x in nums_range if x % 2 == 1]) or 0