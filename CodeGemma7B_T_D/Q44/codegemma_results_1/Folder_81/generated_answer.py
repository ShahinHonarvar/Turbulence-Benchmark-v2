from math import sqrt
from itertools import count

def is_prime(k):
    if k % 2 == 0:
        return False
    for i in range(3, int(sqrt(k)) + 1, 2):
        if k % i == 0:
            return False
    return True

def composite_nums_between_indices(nums):
    comp_nums = set()
    for i in range(20, 201):
        if not is_prime(i):
            comp_nums.add(i)
    return comp_nums