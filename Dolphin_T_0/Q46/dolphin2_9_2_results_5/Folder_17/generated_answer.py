def gcf_three_nums(nums):
    num1 = nums[20]
    num2 = nums[51]
    num3 = nums[62]
    i = 1
    gcf = 1
    while i <= min(num1, num2, num3):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            gcf = i
        i += 1
    return gcf