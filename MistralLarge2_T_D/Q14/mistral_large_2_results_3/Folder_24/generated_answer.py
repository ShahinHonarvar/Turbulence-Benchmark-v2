def find_second_smallest_num(nums):
    if len(nums) <= 23:
        return None
    subset = sorted(nums[23:24])
    if len(subset) < 2:
        return None
    return subset[1]