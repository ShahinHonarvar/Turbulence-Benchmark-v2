import functools

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def gcf_two_nums(nums):
    return functools.reduce(lcm, [nums[7], nums[9]]) // gcd(nums[7], nums[9])