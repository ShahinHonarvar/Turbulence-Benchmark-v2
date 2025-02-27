def find_second_smallest_num(nums):
    if len(nums) < 52:
        return None
    subset = sorted(nums[29:52])
    if len(subset) < 2:
        return None
    return subset[1]