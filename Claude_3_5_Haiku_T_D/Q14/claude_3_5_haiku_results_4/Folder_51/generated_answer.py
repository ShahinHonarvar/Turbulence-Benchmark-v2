def find_second_smallest_num(nums):
    if len(nums) < 9:
        return None
    subset = nums[1:9]
    if len(set(subset)) < 2:
        return None
    sorted_subset = sorted(set(subset))
    return sorted_subset[1] if len(sorted_subset) > 1 else None