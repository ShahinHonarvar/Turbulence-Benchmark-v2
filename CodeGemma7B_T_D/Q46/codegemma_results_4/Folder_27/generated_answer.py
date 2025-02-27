def gcf_three_nums(nums):
    num1 = nums[76]
    num2 = nums[64]
    num3 = nums[28]
    gcd = gcf(num1, gcf(num2, num3))
    return gcd