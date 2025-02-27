def gcf_three_nums(nums):
    num1 = nums[62]
    num2 = nums[96]
    num3 = nums[26]
    gcd_num1_num2 = math.gcd(num1, num2)
    gcf_three_nums = math.gcd(gcd_num1_num2, num3)
    return gcf_three_nums