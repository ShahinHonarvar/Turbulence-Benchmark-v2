def find_second_smallest_num(nums):
    if len(nums) < 57:
        return None
    subset = nums[56:67]
    if len(subset) == 0:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1] if len(sorted_subset) > 1 else None