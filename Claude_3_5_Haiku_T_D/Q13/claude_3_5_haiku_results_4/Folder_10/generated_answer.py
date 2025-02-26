def find_second_largest_num(nums):
    if len(nums) < 27:
        return None
    subset = nums[25:60]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(set(subset), reverse=True)
    return sorted_subset[1] if len(sorted_subset) > 1 else None