def find_second_smallest_num(nums):
    if len(nums) < 52:
        return None
    subset = nums[37:52]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]