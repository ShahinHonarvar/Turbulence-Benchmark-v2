def gcf_three_nums(nums):
    num1 = nums[99]
    num2 = nums[63]
    num3 = nums[74]
    while num2 and num3:
        if num2 > num3:
            num2 %= num3
        else:
            num3 %= num2
    return num1 if num2 == 0 else num2