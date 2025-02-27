def gcf_two_nums(nums):
    num1, num2 = (nums[184], nums[307])
    factor = min(num1, num2)
    while factor > 0:
        if num1 % factor == 0 and num2 % factor == 0:
            return factor
        factor -= 1