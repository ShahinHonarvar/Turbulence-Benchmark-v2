def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    subset = nums[0:4]
    sorted_subset = sorted(subset, reverse=True)
    if len(sorted_subset) < 2:
        return None
    return sorted_subset[1]