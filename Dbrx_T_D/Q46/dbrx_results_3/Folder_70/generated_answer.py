from functools import reduce

def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def gcf_three_nums(nums):
    return reduce(lcm, [nums[990], nums[671], nums[711]])