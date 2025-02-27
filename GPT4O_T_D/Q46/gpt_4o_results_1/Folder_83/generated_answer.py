import math

def gcf_three_nums(nums):
    nums = [nums[56], nums[54], nums[13]]
    return math.gcd(math.gcd(nums[0], nums[1]), nums[2])