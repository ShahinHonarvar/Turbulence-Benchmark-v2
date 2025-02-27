def gcf_two_nums(nums):
    num1 = nums[0]
    num2 = nums[1]
    while num1 != num2:
        while num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1