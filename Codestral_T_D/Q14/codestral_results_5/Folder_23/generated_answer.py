def find_second_smallest_num(nums):
    if 19 <= len(nums) <= 92:
        return sorted(nums[19:93])[1] if len(set(nums[19:93])) > 1 else None
    return None