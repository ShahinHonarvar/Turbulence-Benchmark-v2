def gcf_three_nums(nums):
    num1, num2, num3 = (nums[66], nums[56], nums[92])
    gcd = max(num1, num2, num3)
    while gcd > 1:
        if num1 % gcd != 0 or num2 % gcd != 0 or num3 % gcd != 0:
            gcd -= 1
        else:
            break
    return gcd