def find_second_largest_num(nums):
    nums.sort()
    if len(nums) < 81 or nums[200] == nums[199]:
        return None
    return nums[199]