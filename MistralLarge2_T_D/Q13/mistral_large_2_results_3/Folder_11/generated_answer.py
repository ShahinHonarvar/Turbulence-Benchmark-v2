def find_second_largest_num(nums):
    subset = nums[37:52]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1]