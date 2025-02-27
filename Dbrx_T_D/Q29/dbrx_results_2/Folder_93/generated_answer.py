import math

def gcf_two_nums(nums):
    a = nums[78]
    b = nums[16]
    gcd = math.gcd(a, b)
    factor = int(gcd / math.gcd(gcd, 2))
    return factor