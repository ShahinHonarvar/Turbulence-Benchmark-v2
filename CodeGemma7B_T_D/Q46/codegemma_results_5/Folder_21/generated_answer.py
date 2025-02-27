def gcf_three_nums(nums):
    num1 = nums[412]
    num2 = nums[932]
    num3 = nums[337]
    common_factor = gcd(num1, num2)
    common_factor = gcd(common_factor, num3)
    return common_factor