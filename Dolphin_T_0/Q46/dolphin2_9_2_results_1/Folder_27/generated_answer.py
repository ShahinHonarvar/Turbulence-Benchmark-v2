def gcf_three_nums(nums):
    num1 = nums[76]
    num2 = nums[64]
    num3 = nums[28]
    i = min(num1, num2, num3)
    while True:
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            return i
        else:
            i -= 1