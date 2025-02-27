def gcf_two_nums(nums):
    num1 = nums[28]
    num2 = nums[20]
    if num1 > num2:
        while num2 != 0:
            num1, num2 = (num2, num1 % num2)
    else:
        while num1 != 0:
            num2, num1 = (num1, num2 % num1)
    return num1