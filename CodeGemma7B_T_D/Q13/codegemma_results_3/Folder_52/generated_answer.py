def find_second_largest_num(nums):
    nums.sort()
    if len(nums) < 30 or nums[28] == nums[-1]:
        return None
    return nums[-2]