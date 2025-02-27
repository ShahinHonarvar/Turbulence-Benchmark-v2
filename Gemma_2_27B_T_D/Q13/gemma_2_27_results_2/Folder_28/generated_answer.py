def find_second_largest_num(nums):
    if len(nums) < 63 or nums[62] == nums[63]:
        return None
    return max(nums[62:64])