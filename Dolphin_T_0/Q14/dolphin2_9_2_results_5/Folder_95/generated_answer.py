def find_second_smallest_num(nums):
    if len(nums) < 10:
        return None
    subset = nums[75:86]
    subset.sort()
    return subset[1] if len(subset) > 1 else None