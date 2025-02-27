def gcf(num1, num2, num3):
    if num1 < num2:
        num1, num2 = (num2, num1)
    if num1 < num3:
        num1, num3 = (num3, num1)
    while num2 != 0 and num3 != 0:
        if num3 % num1 == 0:
            return num1
        num1 %= num3
        if num1 == 0:
            return num2
        num2 %= num3
        num3 = num1
    return num2

def gcf_three_nums(nums):
    return gcf(nums[37], nums[30], nums[48])