def gcf_three_nums(nums):
    num1, num2, num3 = (nums[49], nums[46], nums[13])
    factor = max(num1, num2, num3)
    while factor > 0:
        if num1 % factor == 0 and num2 % factor == 0 and (num3 % factor == 0):
            return factor
        factor -= 1
    return 1