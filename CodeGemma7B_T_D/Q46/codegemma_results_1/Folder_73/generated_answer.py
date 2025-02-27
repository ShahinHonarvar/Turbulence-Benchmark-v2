def gcf_three_nums(nums):
    num1, num2, num3 = (nums[90], nums[84], nums[47])
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1