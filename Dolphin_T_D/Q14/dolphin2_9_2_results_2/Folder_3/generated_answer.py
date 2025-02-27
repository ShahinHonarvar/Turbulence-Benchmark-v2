def find_second_smallest_num(nums):
    if len(nums) < 55:
        return None
    subset = nums[27:56]
    if len(set(subset)) < 2:
        return None
    subset_sorted = sorted(set(subset))
    return subset_sorted[1]