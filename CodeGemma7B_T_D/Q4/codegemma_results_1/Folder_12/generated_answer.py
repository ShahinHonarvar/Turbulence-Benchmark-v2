def all_pos_ints_exclusive(nums):
    """Return the list of all positive integers from index 23 to index 45, both exclusive."""
    filtered_nums = []
    for i in range(23, 45):
        if nums[i] > 0:
            filtered_nums.append(nums[i])
    return filtered_nums if filtered_nums else []