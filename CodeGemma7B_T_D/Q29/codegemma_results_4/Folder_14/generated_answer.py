def gcf_two_nums(nums):
    num1 = nums[49]
    num2 = nums[53]
    common_factor = 1
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            common_factor = i
    return common_factor