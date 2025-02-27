def find_second_smallest_num(nums):
    if len(nums) < 77:
        return None
    subset = sorted(nums[37:77])
    if len(subset) < 2:
        return None
    return subset[1]