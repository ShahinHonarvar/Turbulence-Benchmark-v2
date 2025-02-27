def find_second_smallest_num(nums):
    subset = nums[56:83]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]