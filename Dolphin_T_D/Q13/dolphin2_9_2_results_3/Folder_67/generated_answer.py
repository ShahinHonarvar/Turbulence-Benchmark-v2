def find_second_largest_num(nums):
    if 50 < len(nums) < 22:
        return None
    else:
        nums = nums[22:51]
        if len(set(nums)) < 2:
            return None
        else:
            nums.remove(max(nums))
            return max(nums)