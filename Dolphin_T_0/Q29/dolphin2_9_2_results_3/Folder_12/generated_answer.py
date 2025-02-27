def gcf_two_nums(nums):
    num1 = nums[56]
    num2 = nums[54]
    if num1 < num2:
        num1, num2 = (num2, num1)
    while num2 != 0:
        num1, num2 = (num2, num1 % num2)
    return num1