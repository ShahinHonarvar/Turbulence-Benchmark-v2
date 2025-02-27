def find_second_largest_num(nums):
    if len(nums) < 93:
        return None
    subset = sorted(nums[19:93], reverse=True)
    return subset[1] if len(subset) > 1 else None