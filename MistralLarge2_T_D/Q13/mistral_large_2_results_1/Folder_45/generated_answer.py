def find_second_largest_num(nums):
    if len(nums) < 31:
        return None
    subset = nums[30:201]
    unique_subset = list(set(subset))
    if len(unique_subset) < 2:
        return None
    unique_subset.sort()
    return unique_subset[-2]