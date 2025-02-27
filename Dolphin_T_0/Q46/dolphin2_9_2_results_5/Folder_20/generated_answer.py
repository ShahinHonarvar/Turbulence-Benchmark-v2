def gcf_three_nums(nums):
    num1 = nums[29]
    num2 = nums[53]
    num3 = nums[42]
    i = min(num1, num2, num3)
    while i >= 1:
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            return i
        i -= 1
    return 1