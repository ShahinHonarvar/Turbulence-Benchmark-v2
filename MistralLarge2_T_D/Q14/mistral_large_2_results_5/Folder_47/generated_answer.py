def find_second_smallest_num(nums):
    if len(nums) <= 63:
        return None
    subset = sorted(nums[22:64])
    if len(subset) < 2:
        return None
    return subset[1]