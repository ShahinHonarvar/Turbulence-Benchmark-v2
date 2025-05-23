def find_second_largest_num(nums):
    if len(nums) < 41 or len(nums) <= 28:
        return None
    subset = nums[28:41]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(set(subset), reverse=True)
    return sorted_subset[1] if len(sorted_subset) >= 2 else None