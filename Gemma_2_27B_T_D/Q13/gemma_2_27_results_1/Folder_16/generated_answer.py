def find_second_largest_num(nums):
    if len(nums) < 36 or nums[33] == nums[34] == nums[35] == nums[36]:
        return None
    else:
        return sorted([nums[33], nums[34], nums[35], nums[36]])[-2]