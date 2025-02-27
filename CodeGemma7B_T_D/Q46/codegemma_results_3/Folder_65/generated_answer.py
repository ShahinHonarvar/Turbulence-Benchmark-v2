def gcf_three_nums(nums):
    a = nums[18]
    b = nums[10]
    c = nums[76]
    common_factor = 1
    for i in range(2, min([a, b, c]) + 1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            common_factor = i
    return common_factor