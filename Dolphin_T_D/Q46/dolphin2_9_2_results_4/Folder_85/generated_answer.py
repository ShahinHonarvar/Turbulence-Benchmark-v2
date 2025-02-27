def gcf_three_nums(nums):
    num1 = nums[49]
    num2 = nums[46]
    num3 = nums[13]
    gcf = min(num1, num2, num3)
    while True:
        if num1 % gcf == 0 and num2 % gcf == 0 and (num3 % gcf == 0):
            return gcf
        else:
            gcf -= 1