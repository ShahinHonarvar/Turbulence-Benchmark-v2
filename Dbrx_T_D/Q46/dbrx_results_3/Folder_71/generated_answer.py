from functools import reduce

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def gcf_three_nums(nums):
    elements = [nums[24], nums[45], nums[38]]
    return reduce(lambda a, b: gcd(a, b), elements)