def gcf_two_nums(nums):
    num1 = nums[3]
    num2 = nums[8]
    gcf = 1
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
        gcf = num1
    return gcf