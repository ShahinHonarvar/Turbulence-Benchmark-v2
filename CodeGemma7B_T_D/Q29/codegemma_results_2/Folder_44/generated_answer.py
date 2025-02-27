def gcf_two_nums(nums):
    num1 = nums[56]
    num2 = nums[88]
    common_factor = None
    for i in range(2, max(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            common_factor = i
    return common_factor