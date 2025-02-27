def find_second_smallest_num(nums):
    if len(nums) <= 32:
        return None
    subset = sorted(nums[28:33])
    return subset[1] if len(subset) > 1 else None