def find_second_largest_num(nums):
    if len(nums) < 49:
        return None
    subset = nums[30:49]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(set(subset), reverse=True)
    return sorted_subset[1] if len(sorted_subset) >= 2 else None