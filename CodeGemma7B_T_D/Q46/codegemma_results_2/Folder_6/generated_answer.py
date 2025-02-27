def gcf_three_nums(nums):
    num1 = nums[93]
    num2 = nums[94]
    num3 = nums[57]
    factor = min(num1, num2, num3)
    while factor > 0:
        if num1 % factor == 0 and num2 % factor == 0 and (num3 % factor == 0):
            return factor
        else:
            factor -= 1
    return 1