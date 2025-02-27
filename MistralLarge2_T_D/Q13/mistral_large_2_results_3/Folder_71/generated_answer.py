def find_second_largest_num(nums):
    if len(nums) <= 52:
        return None
    subset = nums[26:53]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1]