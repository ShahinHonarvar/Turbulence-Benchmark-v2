def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    elif len(nums) == 2:
        return min(nums)
    else:
        nums = sorted(nums, reverse=True)
        return nums[1]