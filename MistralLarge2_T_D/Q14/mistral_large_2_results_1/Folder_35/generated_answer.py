def find_second_smallest_num(nums):
    if len(nums) < 40:
        return None
    subset = sorted(nums[15:40])
    if len(subset) < 2:
        return None
    return subset[1]