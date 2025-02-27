def find_second_largest_num(nums):
    if len(nums) < 2 or nums[6] == nums[7]:
        return None
    else:
        return max(nums[6], nums[7])