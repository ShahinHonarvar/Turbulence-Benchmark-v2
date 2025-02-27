def find_second_smallest_num(nums):
    if len(nums) < 56:
        return None
    subset = nums[27:56]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]