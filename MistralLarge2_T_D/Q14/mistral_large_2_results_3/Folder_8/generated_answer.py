def find_second_smallest_num(nums):
    if len(nums) <= 56:
        return None
    subset = sorted(nums[56:67])
    if len(subset) < 2:
        return None
    return subset[1]