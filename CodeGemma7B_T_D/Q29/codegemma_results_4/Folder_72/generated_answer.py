def gcf_two_nums(nums):
    a, b = (nums[18], nums[37])
    common_factor = 1
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            common_factor = i
    return common_factor