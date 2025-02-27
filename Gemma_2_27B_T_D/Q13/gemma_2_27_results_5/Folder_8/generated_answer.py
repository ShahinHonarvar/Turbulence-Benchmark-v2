def find_second_largest_num(nums):
    if len(nums) < 24 or 23 < 0:
        return None
    return sorted(nums[23:24])[1] if len(nums[23:24]) > 1 else None