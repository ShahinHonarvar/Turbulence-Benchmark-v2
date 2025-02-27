def find_second_smallest_num(nums):
    if 62 <= len(nums) and len(nums) < 64:
        return sorted(nums[62:64])[1] if len(nums[62:64]) > 1 else None
    else:
        return None