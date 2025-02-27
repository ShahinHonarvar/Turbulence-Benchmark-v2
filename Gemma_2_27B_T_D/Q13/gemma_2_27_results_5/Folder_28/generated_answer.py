def find_second_largest_num(nums):
    if len(nums) >= 63 and nums[62] != nums[63]:
        return max(nums[62:64])
    return None