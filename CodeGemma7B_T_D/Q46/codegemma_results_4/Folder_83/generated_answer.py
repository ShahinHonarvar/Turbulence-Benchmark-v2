def gcf_three_nums(nums):
    num1 = nums[56]
    num2 = nums[54]
    num3 = nums[13]
    gcd = 0
    i = 0
    while i <= num2:
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            gcd = i
        i += 1
    return gcd