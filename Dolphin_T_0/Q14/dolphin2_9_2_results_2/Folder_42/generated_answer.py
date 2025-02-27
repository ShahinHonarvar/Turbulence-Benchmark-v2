def find_second_smallest_num(nums):
    if 21 <= len(nums) <= 97:
        return sorted(nums[21:98])[1] if len(nums[21:98]) > 1 else None
    else:
        return None