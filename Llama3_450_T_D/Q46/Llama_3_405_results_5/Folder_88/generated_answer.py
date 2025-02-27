import math

def gcf_three_nums(nums):
    nums = [nums[47], nums[10], nums[28]]

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    result = nums[0]
    for num in nums[1:]:
        result = gcd(result, num)
    return result