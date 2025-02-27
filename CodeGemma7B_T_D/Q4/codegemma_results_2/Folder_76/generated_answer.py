def all_pos_ints_exclusive(nums):
    filtered_nums = [num for num in nums[361:644] if num > 0]
    return filtered_nums if filtered_nums else []