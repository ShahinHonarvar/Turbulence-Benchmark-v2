def gcf_two_nums(nums):
    common_factor = 1
    for i in range(3, 5):
        common_factor = min(common_factor, max(nums[45][i], nums[12][i]))
    return common_factor