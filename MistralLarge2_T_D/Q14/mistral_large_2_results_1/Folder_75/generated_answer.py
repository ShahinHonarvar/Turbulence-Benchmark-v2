def find_second_smallest_num(nums):
    if len(nums) < 92:
        return None
    subset = sorted(nums[12:93])
    return subset[1] if len(subset) > 1 else None