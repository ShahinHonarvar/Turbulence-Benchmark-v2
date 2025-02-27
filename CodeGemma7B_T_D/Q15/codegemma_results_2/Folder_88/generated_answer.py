from functools import reduce

def sum_odd_ints_inclusive(nums):
    return reduce(lambda x, y: x + y, filter(lambda x: x % 2 != 0 and 4 <= x <= 8, nums))