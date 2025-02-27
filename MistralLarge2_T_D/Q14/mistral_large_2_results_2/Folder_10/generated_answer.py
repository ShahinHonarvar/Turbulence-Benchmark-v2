def find_second_smallest_num(nums):
    if len(nums) < 93:
        return None
    subset = nums[62:93]
    if len(subset) < 2:
        return None
    unique_nums = sorted(set(subset))
    if len(unique_nums) < 2:
        return None
    return unique_nums[1]