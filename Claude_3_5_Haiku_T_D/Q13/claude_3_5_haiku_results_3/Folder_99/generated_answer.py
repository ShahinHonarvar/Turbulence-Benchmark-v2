def find_second_largest_num(nums):
    if not nums or len(nums) < 312:
        return None
    subset = nums[310:371]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(set(subset), reverse=True)
    return sorted_subset[1] if len(sorted_subset) >= 2 else None