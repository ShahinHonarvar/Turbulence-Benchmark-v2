from math import gcd

def gcf_three_nums(nums):
    arg1, arg2, arg3 = (nums[341], nums[238], nums[374])
    return gcd(arg1, gcd(arg2, arg3))