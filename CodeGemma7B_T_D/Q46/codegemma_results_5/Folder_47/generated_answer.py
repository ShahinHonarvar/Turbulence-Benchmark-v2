def gcf_three_nums(nums):
    num1 = nums[36]
    num2 = nums[85]
    num3 = nums[83]
    factor = 1
    while factor <= num1 and factor <= num2 and (factor <= num3):
        if num1 % factor == 0 and num2 % factor == 0 and (num3 % factor == 0):
            gcf = factor
        factor += 1
    return gcf