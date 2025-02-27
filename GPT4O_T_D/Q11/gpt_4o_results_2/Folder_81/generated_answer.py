def find_largest_num(nums):
    if len(nums) >= 101:
        return max(nums[10:101])
    return None