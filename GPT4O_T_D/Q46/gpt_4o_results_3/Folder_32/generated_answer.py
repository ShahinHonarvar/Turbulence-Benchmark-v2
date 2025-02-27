import math

def gcf_three_nums(nums):
    if len(nums) > 95:
        return math.gcd(math.gcd(nums[20], nums[43]), nums[95])
    return None