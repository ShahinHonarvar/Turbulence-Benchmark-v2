def find_second_smallest_num(nums):
    if len(nums) < 63 or max(nums) <= 62 or min(nums) >= 93:
        return None
    return sorted(nums[62:93])[1]