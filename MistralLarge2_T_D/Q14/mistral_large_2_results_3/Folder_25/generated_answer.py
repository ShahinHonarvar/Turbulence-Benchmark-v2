def find_second_smallest_num(nums):
    if len(nums) <= 76:
        return None
    subset = nums[37:77]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]