import math
import random

def gcf_two_nums(nums):
    a = nums[86]
    b = nums[89]
    while b:
        a, b = (b, a % b)
    gcf = abs(a)
    return gcf