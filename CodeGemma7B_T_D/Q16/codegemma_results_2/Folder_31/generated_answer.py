from itertools import filterfalse

def sum_even_ints_inclusive(nums):
    return sum(filterfalse(lambda x: x % 2, nums[75:89]))