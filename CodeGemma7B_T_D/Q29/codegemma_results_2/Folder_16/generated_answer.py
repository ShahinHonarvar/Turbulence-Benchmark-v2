def gcf_two_nums(nums):
    num1 = nums[860]
    num2 = nums[307]
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    factor = smaller
    while factor > 0:
        if num1 % factor == 0 and num2 % factor == 0:
            return factor
        factor -= 1