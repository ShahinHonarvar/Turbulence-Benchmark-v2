def find_second_smallest_num(nums):
    if len(nums) < 67:
        return None
    subset = nums[10:67]
    if len(subset) == 0:
        return None
    sorted_subset = sorted(subset)
    if len(sorted_subset) < 2:
        return None
    return sorted_subset[1]