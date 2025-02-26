def find_second_largest_num(nums):
    if len(nums) < 2 or len(nums) <= 7:
        return None
    subset = nums[0:8]
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1] if len(sorted_subset) > 1 else None