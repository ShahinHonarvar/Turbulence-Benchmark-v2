def gcf_three_nums(nums):
    a, b, c = (nums[9], nums[6], nums[2])
    common_factor = max(a % b, b % c, c % a)
    return common_factor