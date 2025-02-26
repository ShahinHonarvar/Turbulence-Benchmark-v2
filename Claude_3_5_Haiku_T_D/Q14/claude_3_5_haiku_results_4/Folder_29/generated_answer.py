def find_second_smallest_num(nums):
    if len(nums) < 56:
        return None
    subset = nums[55:99]
    if len(subset) == 0:
        return None
    sorted_subset = sorted(subset)
    if len(sorted_subset) < 2:
        return None
    return sorted_subset[1]