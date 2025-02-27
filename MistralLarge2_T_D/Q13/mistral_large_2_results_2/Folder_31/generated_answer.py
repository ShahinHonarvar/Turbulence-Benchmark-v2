def find_second_largest_num(nums):
    subset = nums[75:89]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[-2]