from functools import reduce
import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def gcf_two_nums(nums):
    return math.gcd(nums[33], nums[85]) if all((x > 0 for x in [nums[33], nums[85]])) else 0