def find_second_largest_num(nums):
    nums = sorted(nums, reverse=True)[12:93]
    return nums[1] if len(nums) > 1 else 'None'