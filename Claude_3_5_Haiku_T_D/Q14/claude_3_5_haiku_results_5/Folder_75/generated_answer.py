def find_second_smallest_num(nums):
    if len(nums) < 94:
        return None
    subset = nums[12:93]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]