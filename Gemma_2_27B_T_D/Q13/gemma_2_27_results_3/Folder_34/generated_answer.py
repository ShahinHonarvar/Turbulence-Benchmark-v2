def find_second_largest_num(nums):
    if len(nums) < 46 or len(set(nums[16:62])) < 2:
        return None
    return sorted(set(nums[16:62]))[-2]