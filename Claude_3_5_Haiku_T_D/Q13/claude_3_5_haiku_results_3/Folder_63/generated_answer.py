def find_second_largest_num(nums):
    if len(nums) < 23 or 88 >= len(nums):
        return None
    subset = nums[22:89]
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1] if len(sorted_subset) > 1 else None