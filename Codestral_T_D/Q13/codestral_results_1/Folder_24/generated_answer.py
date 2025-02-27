def find_second_largest_num(nums):
    subset = nums[74:96]
    sorted_subset = sorted(subset, reverse=True)
    if len(sorted_subset) < 2:
        return None
    else:
        return sorted_subset[1]