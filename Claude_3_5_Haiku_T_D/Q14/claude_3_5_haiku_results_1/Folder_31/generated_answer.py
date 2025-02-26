def find_second_smallest_num(nums):
    if len(nums) < 94:
        return None
    subset = nums[29:94]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(set(subset))
    return sorted_subset[1] if len(sorted_subset) >= 2 else None