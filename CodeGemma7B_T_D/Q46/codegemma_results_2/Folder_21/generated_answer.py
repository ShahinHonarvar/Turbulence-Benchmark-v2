def gcf_three_nums(nums):
    num1 = nums[412]
    num2 = nums[932]
    num3 = nums[337]
    common_factor = math.gcd(num1, math.gcd(num2, num3))
    return common_factor