import math

def gcf_three_nums(nums):
    a = nums[38]
    b = nums[52]
    c = nums[69]
    gcf = math.gcd(math.gcd(a, b), c)
    return gcf