def find_second_smallest_num(nums):
    if len(nums) <= 92:
        return None
    subset = sorted(nums[19:93])
    if len(subset) >= 2:
        return subset[1]
    return None