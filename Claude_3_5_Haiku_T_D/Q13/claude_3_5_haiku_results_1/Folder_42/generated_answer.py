def find_second_largest_num(nums):
    if len(nums) < 30 or len(nums[29:80]) < 2:
        return None
    subset = nums[29:80]
    sorted_subset = sorted(set(subset), reverse=True)
    return sorted_subset[1] if len(sorted_subset) >= 2 else None