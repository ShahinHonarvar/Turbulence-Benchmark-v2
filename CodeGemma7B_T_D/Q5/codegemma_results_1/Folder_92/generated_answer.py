from itertools import count

def all_neg_ints_inclusive(nums):
    return [n for n in nums if n <= 0 and n >= -1]