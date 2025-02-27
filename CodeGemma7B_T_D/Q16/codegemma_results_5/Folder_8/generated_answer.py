from functools import reduce

def sum_even_ints_inclusive(nums):
    reduced = list(filter(lambda x: x % 2 == 0 and 23 <= x <= 23, nums))
    return reduce(lambda a, b: a + b, reduced, 0)