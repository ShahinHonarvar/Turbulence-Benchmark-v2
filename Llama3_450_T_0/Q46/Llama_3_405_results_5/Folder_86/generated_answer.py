import math

def gcf_three_nums(nums):
    num1 = nums[341]
    num2 = nums[238]
    num3 = nums[374]
    gcf12 = math.gcd(num1, num2)
    return math.gcd(gcf12, num3)