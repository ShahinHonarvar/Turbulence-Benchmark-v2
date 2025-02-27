def gcf_three_nums(nums):
    num1 = nums[66]
    num2 = nums[56]
    num3 = nums[92]
    factor = 1
    while factor <= min(num1, num2, num3):
        if num1 % factor == 0 and num2 % factor == 0 and (num3 % factor == 0):
            common_factor = factor
            factor += 1
        else:
            factor += 1
    return common_factor