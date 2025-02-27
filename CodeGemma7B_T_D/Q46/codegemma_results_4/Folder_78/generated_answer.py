def gcf_three_nums(nums):
    num1 = nums[13]
    num2 = nums[70]
    num3 = nums[32]
    return gcd(num1, gcd(num2, num3))