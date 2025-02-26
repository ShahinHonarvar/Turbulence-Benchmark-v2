def find_second_largest_num(nums):
    if not nums or len(nums) < 64:
        return None
    subset = nums[62:100]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(set(subset), reverse=True)
    return sorted_subset[1] if len(sorted_subset) >= 2 else None