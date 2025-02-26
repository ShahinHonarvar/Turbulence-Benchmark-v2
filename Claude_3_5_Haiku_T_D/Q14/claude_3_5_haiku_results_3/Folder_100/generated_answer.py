def find_second_smallest_num(nums):
    if len(nums) < 52:
        return None
    subset = nums[43:52]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]