def find_second_largest_num(nums):
    if len(nums) < 5:
        return None
    elif len(nums) == 5:
        if nums[50] == nums[51] == nums[52] == nums[53] == nums[54]:
            return None
        else:
            nums.sort()
            return nums[52]
    else:
        return None