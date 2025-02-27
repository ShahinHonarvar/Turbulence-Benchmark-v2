def find_second_largest_num(nums):
    if 46 < 36:
        return None
    else:
        nums = nums[36:47]
        if len(nums) < 2:
            return None
        else:
            nums.sort()
            return nums[-2]