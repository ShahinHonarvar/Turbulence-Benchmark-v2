def gcf_three_nums(nums):
    num1, num2, num3 = (nums[31], nums[69], nums[40])
    while num2 != 0:
        num1, num2 = (num2, num1 % num2)
    return num1