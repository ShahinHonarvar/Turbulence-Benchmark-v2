def find_second_smallest_num(nums):
    subset = nums[639:976]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]