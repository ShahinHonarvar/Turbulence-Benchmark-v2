import math

def gcf_three_nums(nums):
    if len(nums) > max(876, 203, 100):
        return math.gcd(math.gcd(nums[876], nums[203]), nums[100])
    else:
        raise ValueError('List does not contain enough elements.')