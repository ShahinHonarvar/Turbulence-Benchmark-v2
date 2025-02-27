from functools import reduce

def sum_in_range(nums):
    return reduce(lambda x, y: x + y, [n for n in nums if 60 <= n <= 97])