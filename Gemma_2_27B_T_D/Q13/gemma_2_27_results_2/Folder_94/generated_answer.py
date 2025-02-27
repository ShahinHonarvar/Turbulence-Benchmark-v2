def find_second_largest_num(nums):
    if len(nums) < 40 and len(nums) >= 28:
        return sorted(nums[28:41])[-2]
    return None