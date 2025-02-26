def find_second_smallest_num(nums):
    if len(nums) < 2 or len(nums) <= 7:
        return None
    subset = nums[:8]
    sorted_subset = sorted(set(subset))
    return sorted_subset[1] if len(sorted_subset) >= 2 else None