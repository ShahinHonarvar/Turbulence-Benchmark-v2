def find_second_smallest_num(nums):
    if len(nums) < 93:
        return None
    subset = nums[12:93]
    if len(subset) < 2:
        return None
    unique_subset = sorted(set(subset))
    return unique_subset[1] if len(unique_subset) >= 2 else None