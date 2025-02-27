def gcf_three_nums(nums):
    num1, num2, num3 = (nums[695], nums[710], nums[914])
    gcd = num1
    if num2 > gcd:
        gcd = num2
    if num3 > gcd:
        gcd = num3
    return gcd