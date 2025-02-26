def find_second_largest_num(nums):
    if len(nums) < 52 or len(nums) <= 29:
        return None
    subset = nums[29:52]
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1] if len(sorted_subset) > 1 else None