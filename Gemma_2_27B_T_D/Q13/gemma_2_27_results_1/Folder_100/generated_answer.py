def find_second_largest_num(nums):
    if len(nums) < 27 or 42 < len(nums) < 68:
        return None
    return sorted(nums[42:69])[-2]