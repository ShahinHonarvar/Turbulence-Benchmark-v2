def gcf_three_nums(nums):
    num1, num2, num3 = (nums[19], nums[69], nums[97])
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1