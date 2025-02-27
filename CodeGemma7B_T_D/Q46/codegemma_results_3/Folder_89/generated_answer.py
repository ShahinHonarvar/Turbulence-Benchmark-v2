def gcf_three_nums(nums):
    num1 = nums[63]
    num2 = nums[73]
    num3 = nums[11]
    common_factor = gcf(num1, num2)
    return gcf(common_factor, num3)