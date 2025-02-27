def gcf_two_nums(nums):
    num1 = nums[279]
    num2 = nums[812]
    while num2 != 0:
        num1, num2 = (num2, num1 % num2)
    return num1