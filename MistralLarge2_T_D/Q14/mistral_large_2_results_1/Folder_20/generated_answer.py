def find_second_smallest_num(nums):
    if len(nums) >= 95:
        subset = nums[75:95]
        if len(set(subset)) >= 2:
            sorted_subset = sorted(subset)
            return sorted_subset[1]
    return None