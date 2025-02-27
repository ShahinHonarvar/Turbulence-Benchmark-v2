def gcf_three_nums(nums):
    num1 = nums[19]
    num2 = nums[94]
    num3 = nums[78]
    return gcd(num1, gcd(num2, num3))