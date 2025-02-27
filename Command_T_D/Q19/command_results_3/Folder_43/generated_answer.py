import math

def all_ints_not_div_by_num(nums):
    return [x for x in nums[16:87] if math.gcd(x, -15) != 1]