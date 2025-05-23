def gcf_two_nums(nums):
    num1 = nums[180]
    num2 = nums[312]
    for i in range(min(num1, num2), 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i
    return 1