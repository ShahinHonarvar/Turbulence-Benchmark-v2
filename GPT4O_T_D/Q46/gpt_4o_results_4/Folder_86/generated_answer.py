import math

def gcf_three_nums(nums):
    if len(nums) <= max(341, 238, 374):
        return None
    return math.gcd(math.gcd(nums[341], nums[238]), nums[374])