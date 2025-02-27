def find_second_smallest_num(nums):
    if 28 < len(nums) < 41:
        subset = nums[28:41]
        subset.sort()
        if len(subset) > 1:
            return subset[1]
    return None