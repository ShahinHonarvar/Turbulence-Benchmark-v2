def gcf_two_nums(nums):
    num1 = nums[28]
    num2 = nums[17]
    gcd = 1
    lower = min(num1, num2)
    for i in range(2, lower + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
    return gcd