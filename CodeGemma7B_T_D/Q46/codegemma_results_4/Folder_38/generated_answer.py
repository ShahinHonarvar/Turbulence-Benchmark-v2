def gcf_three_nums(nums):
    num1, num2, num3 = (nums[14], nums[21], nums[17])
    while num2 != 0:
        num1, num2 = (num2, num1 % num2)
    while num3 != 0:
        num2, num3 = (num3, num2 % num3)
    return num2