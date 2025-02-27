from functools import reduce

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_three_nums(nums):
    return reduce(gcd, [nums[637], nums[411], nums[757]])