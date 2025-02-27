def find_second_smallest_num(nums):
    if len(nums) < 32 or nums[28] == nums[29] == nums[30] == nums[31] == nums[32]:
        return None
    else:
        return sorted(nums[28:33])[1]