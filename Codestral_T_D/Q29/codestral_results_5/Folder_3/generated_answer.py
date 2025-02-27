def gcf_two_nums(nums):
    num1 = nums[47]
    num2 = nums[10]
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1