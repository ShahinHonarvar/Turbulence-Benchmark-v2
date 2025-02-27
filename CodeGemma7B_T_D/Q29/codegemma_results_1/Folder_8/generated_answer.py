def gcf_two_nums(nums):
    num1 = nums[69]
    num2 = nums[41]
    gcd = 1
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    gcd = num1
    return gcd