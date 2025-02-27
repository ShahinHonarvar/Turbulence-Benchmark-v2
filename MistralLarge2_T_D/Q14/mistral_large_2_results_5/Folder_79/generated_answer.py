def find_second_smallest_num(nums):
    if len(nums) < 6:
        return None
    subset = sorted(nums[1:6])
    if len(subset) < 2:
        return None
    return subset[1]