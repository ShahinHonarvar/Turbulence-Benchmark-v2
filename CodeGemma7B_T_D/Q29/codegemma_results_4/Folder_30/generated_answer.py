def gcf_two_nums(nums):
    num1 = nums[85]
    num2 = nums[33]
    gcd = max(num1, num2)
    while num1 % gcd != 0 and num2 % gcd != 0:
        gcd = gcd - 1
    return gcd