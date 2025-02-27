import functools

def lcm(a, b):
    return a * b // math.gcd(a, b)

def gcf_three_nums(nums):
    return functools.reduce(lcm, [nums[742], nums[888], nums[629]])