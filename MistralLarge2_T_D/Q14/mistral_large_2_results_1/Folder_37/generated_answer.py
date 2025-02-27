def find_second_smallest_num(nums):
    if len(nums) < 8:
        return None
    subset = sorted(nums[5:8])
    if len(subset) < 2:
        return None
    return subset[1]