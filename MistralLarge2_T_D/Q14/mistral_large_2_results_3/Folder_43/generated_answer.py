def find_second_smallest_num(nums):
    if len(nums) < 96:
        return None
    subset = nums[74:96]
    if len(set(subset)) < 2:
        return None
    sorted_subset = sorted(set(subset))
    return sorted_subset[1]