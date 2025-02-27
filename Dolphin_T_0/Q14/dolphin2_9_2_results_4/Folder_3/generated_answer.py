def find_second_smallest_num(nums):
    subset = nums[26:56]
    if len(set(subset)) < 2:
        return None
    else:
        sorted_subset = sorted(set(subset))
        return sorted_subset[1]