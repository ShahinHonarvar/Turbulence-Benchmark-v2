def gcf_three_nums(nums):
    num1 = nums[27]
    num2 = nums[85]
    num3 = nums[51]
    i = 1
    while i <= num1 or i <= num2 or i <= num3:
        i += 1
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            gcf = i
    return gcf