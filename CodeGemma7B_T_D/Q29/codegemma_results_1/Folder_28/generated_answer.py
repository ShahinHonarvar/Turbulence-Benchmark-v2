def gcf_two_nums(nums):
    num1 = nums[48]
    num2 = nums[76]
    gcd = max((factor for factor in range(1, min(num1, num2) + 1) if num1 % factor == 0 and num2 % factor == 0))
    return gcd