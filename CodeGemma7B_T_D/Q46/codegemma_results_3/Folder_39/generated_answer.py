def gcf_three_nums(nums):
    num1, num2, num3 = (nums[85], nums[36], nums[54])
    factor = min(num1, num2, num3)
    while factor > 0:
        if num1 % factor == 0 and num2 % factor == 0 and (num3 % factor == 0):
            return factor
        factor -= 1
    return 1