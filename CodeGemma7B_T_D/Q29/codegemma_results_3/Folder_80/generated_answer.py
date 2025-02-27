def gcf_two_nums(nums):
    num1, num2 = (nums[95], nums[85])
    gcd = 0
    while num1 % gcd != 0 or num2 % gcd != 0:
        gcd += 1
    return gcd