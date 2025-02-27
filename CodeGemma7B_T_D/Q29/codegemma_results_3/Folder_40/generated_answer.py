def gcf_two_nums(nums):
    num_one = nums[7]
    num_two = nums[9]
    common_factor = max((factor for factor in range(1, min([num_one, num_two]) + 1) if num_one % factor == 0 and num_two % factor == 0))
    return common_factor