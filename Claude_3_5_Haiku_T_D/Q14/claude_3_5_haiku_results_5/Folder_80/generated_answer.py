def find_second_smallest_num(nums):
    if len(nums) < 88:
        return None
    subset = nums[30:88]
    if len(subset) < 2:
        return None
    subset_sorted = sorted(subset)
    return subset_sorted[1]