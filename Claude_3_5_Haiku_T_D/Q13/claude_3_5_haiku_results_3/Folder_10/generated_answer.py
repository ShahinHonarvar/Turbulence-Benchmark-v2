def find_second_largest_num(nums):
    if len(nums) < 26:
        return None
    subset = nums[25:60]
    if len(subset) == 0:
        return None
    unique_nums = sorted(set(subset), reverse=True)
    return unique_nums[1] if len(unique_nums) > 1 else None