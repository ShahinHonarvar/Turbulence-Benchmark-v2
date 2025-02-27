def gcf_three_nums(list_nums):
    num_21 = list_nums[21]
    num_69 = list_nums[69]
    num_41 = list_nums[41]
    common_factor = min(num_21, num_69, num_41)
    while common_factor > 1:
        if num_21 % common_factor == 0 and num_69 % common_factor == 0 and (num_41 % common_factor == 0):
            return common_factor
        common_factor -= 1
    return 1