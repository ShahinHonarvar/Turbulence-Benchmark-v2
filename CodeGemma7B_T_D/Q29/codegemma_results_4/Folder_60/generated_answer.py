def gcf_two_nums(nums):
    num1, num2 = (nums[28], nums[53])
    gcd = 1
    while num2:
        num1, num2 = (num2, num1 % num2)
    return gcd