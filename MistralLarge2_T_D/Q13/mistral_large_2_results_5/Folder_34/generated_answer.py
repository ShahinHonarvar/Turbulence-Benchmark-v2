def find_second_largest_num(nums):
    subset = nums[16:62]
    if len(subset) >= 2:
        sorted_subset = sorted(subset, reverse=True)
        return sorted_subset[1]
    return None