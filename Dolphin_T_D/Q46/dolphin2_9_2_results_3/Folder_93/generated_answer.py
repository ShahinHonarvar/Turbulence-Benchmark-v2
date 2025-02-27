def gcf_three_nums(nums):
    num1 = nums[25]
    num2 = nums[76]
    num3 = nums[57]
    i = min(num1, num2, num3)
    while i > 0:
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            return i
        i -= 1
    return None