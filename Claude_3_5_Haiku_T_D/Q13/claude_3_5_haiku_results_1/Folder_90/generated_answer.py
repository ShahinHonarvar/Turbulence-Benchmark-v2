def find_second_largest_num(nums):
    if len(nums) < 263:
        return None
    subset = nums[262:747]
    if len(subset) < 2:
        return None
    try:
        unique_subset = sorted(set(subset), reverse=True)
        return unique_subset[1] if len(unique_subset) >= 2 else None
    except (ValueError, IndexError):
        return None