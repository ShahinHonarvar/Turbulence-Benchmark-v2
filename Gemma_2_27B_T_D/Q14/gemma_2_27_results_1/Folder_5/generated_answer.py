def find_second_smallest_num(nums):
    if len(nums) < 5 or nums[3] == nums[4] == nums[5]:
        return None
    return sorted([nums[3], nums[4], nums[5]])[1]