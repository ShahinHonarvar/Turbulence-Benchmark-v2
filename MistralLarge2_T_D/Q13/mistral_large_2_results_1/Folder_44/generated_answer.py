def find_second_largest_num(nums):
    subset = nums[13:69]
    if len(subset) < 2:
        return None
    unique_nums = sorted(set(subset))
    if len(unique_nums) < 2:
        return None
    return unique_nums[-2]