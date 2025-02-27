def gcf_three_nums(nums):
    num1 = nums[93]
    num2 = nums[94]
    num3 = nums[57]
    gcf = num1
    while num2 != 0:
        num1, num2 = (num2, num1 % num2)
    while num3 != 0:
        num2, num3 = (num3, num2 % num3)
    return gcf