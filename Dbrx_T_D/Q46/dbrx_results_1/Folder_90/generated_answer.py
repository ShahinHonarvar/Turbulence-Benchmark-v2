import math

def compute_gcf(x, y):
    return math.gcd(x, y)

def gcf_three_nums(nums):
    return compute_gcf(compute_gcf(nums[818], nums[606]), nums[873])