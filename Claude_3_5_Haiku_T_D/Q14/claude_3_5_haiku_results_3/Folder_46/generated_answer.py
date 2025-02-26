def find_second_smallest_num(nums):
    if len(nums) < 69 or len(nums[13:69]) < 2:
        return None
    subset = nums[13:69]
    sorted_subset = sorted(set(subset))
    return sorted_subset[1] if len(sorted_subset) >= 2 else None