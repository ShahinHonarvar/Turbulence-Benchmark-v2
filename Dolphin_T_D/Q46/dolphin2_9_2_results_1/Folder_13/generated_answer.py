def gcf_three_nums(list_nums):
    num1 = list_nums[991]
    num2 = list_nums[244]
    num3 = list_nums[974]
    nums_min = min(num1, num2, num3)
    for i in range(nums_min, 0, -1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            return i
    return 1