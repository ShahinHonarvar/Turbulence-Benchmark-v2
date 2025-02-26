def find_second_largest_num(nums):
    if len(nums) < 22:
        return None
    subset = nums[21:98]
    if len(subset) < 2:
        return None
    unique_subset = sorted(set(subset), reverse=True)
    return unique_subset[1] if len(unique_subset) >= 2 else None