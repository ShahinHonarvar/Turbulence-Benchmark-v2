def find_second_largest_num(nums):
    if len(nums) < 56:
        return None
    subset = nums[34:56]
    if len(subset) == 0:
        return None
    subset.sort(reverse=True)
    if len(subset) < 2:
        return None
    return subset[1]