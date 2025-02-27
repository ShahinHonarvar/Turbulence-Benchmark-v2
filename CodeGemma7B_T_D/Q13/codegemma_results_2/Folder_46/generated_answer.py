def find_second_largest_num(nums):
    nums.sort()
    if len(nums) >= 87 and nums[87] == nums[86]:
        return None
    elif len(nums) >= 30 and nums[30] == nums[29]:
        return None
    else:
        return nums[86]