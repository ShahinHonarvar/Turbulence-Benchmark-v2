def find_second_largest_num(nums):
    if len(nums) < 32 or len(nums) < 28:
        return None
    return sorted(nums[28:33])[-2]