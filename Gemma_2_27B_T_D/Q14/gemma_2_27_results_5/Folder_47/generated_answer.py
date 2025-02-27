def find_second_smallest_num(nums):
    if len(nums) < 63:
        return None
    return sorted(nums[22:64])[1] if len(set(nums[22:64])) > 1 else None