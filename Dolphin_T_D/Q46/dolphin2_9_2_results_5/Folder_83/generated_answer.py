def gcf_three_nums(nums):
    num1 = nums[56]
    num2 = nums[54]
    num3 = nums[13]
    for i in range(min(num1, num2, num3), 1, -1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            return i
    return 1