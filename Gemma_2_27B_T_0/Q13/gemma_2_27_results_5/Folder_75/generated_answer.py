def find_second_largest_num(nums):
    if len(nums) < 57 or 56 < 0:
        return None
    return sorted(nums[56:58])[-2] if len(sorted(nums[56:58])) > 1 else None