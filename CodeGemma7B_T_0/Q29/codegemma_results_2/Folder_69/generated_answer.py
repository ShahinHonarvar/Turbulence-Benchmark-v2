def gcf_two_nums(nums):
    num1 = nums[894]
    num2 = nums[801]
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1