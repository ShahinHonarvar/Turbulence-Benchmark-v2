def find_second_largest_num(nums):
    if len(nums) < 30:
        return None
    return sorted(nums[20:31])[-2] if len(sorted(nums[20:31])) > 1 else None