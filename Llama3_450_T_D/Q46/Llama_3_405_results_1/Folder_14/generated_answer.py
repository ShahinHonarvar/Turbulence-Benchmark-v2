import math

def gcf_three_nums(nums):
    a = nums[17]
    b = nums[88]
    c = nums[35]
    gcf_ab = math.gcd(a, b)
    gcf_abc = math.gcd(gcf_ab, c)
    return gcf_abc