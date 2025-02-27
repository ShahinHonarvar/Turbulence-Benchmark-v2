def find_second_smallest_num(nums):
    if len(nums) < 64:
        return None
    subset = nums[62:64]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]