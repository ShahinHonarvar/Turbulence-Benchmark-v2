def find_second_largest_num(nums):
    if len(nums) < 606:
        return None
    subset = nums[533:606]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[-2]