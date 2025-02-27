def find_second_smallest_num(nums):
    if len(nums) <= 88:
        subset = nums[22:89]
    else:
        subset = nums[22:88]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]