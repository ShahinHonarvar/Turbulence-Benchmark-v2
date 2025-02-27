from functools import reduce

def gcf_three_nums(nums):
    elements = [nums[693], nums[331], nums[668]]
    return reduce(lambda x, y: gcd(x, y), elements)

def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a