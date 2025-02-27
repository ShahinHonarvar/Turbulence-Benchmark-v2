def find_second_smallest_num(nums):
    if len(nums) < 11 or 75 not in range(len(nums)) or 85 not in range(len(nums)):
        return None
    return sorted(nums[75:86])[1]