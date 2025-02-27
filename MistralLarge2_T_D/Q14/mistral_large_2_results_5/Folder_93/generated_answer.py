def find_second_smallest_num(nums):
    if len(nums) < 89:
        return None
    subset = sorted(nums[75:89])
    if len(subset) < 2:
        return None
    return subset[1]