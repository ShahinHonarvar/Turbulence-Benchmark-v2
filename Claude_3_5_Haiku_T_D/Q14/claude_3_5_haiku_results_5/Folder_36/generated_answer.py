def find_second_smallest_num(nums):
    if len(nums) <= 209:
        return None
    subset = nums[209:557]
    if len(subset) == 0:
        return None
    sorted_subset = sorted(subset)
    if len(sorted_subset) < 2:
        return None
    return sorted_subset[1]