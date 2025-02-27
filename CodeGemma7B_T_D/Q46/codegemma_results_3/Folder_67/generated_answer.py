def gcf_three_nums(nums):
    num1 = nums[70]
    num2 = nums[41]
    num3 = nums[20]
    factor = 1
    for i in range(1, min(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            factor = i
    return factor