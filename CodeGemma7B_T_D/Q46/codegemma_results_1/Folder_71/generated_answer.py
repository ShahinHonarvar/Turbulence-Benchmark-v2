def gcf_three_nums(nums):
    num1 = nums[24]
    num2 = nums[45]
    num3 = nums[38]
    gcd = num1
    if num2 > gcd:
        gcd = num2
    if num3 > gcd:
        gcd = num3
    while num1 % gcd != 0 or num2 % gcd != 0 or num3 % gcd != 0:
        gcd -= 1
    return gcd