def find_second_largest_num(nums):
    if len(nums) <= 1 or len(nums) <= 5:
        return None
    subset = nums[0:6]
    sorted_subset = sorted(set(subset), reverse=True)
    return sorted_subset[1] if len(sorted_subset) > 1 else None