def gcf_three_nums(nums):
    num1 = nums[62]
    num2 = nums[96]
    num3 = nums[26]
    common_factor = 1
    while num1 and num2 and num3:
        min_value = min(num1, num2, num3)
        while min_value % num1:
            num1 -= 1
        while min_value % num2:
            num2 -= 1
        while min_value % num3:
            num3 -= 1
        common_factor *= min_value
        num1 = num2 = num3 = min_value
    return common_factor