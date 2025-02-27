def gcf_two_nums(nums):
    num1 = nums[76]
    num2 = nums[57]
    gcd = 1
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
        gcd *= num1 or num2
    return gcd