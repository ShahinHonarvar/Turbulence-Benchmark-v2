def gcf_two_nums(nums):
    num1 = nums[76]
    num2 = nums[57]
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1