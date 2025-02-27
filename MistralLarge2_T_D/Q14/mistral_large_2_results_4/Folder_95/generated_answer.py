def find_second_smallest_num(nums):
    subset = nums[75:86]
    sorted_subset = sorted(subset)
    return sorted_subset[1] if len(sorted_subset) > 1 else None