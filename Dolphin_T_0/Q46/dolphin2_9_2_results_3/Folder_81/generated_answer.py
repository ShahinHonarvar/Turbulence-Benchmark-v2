def gcf_three_nums(nums):
    num1 = nums[20]
    num2 = nums[17]
    num3 = nums[28]
    i = 1
    while i <= num1 and i <= num2 and (i <= num3):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            gcf = i
        i += 1
    return gcf