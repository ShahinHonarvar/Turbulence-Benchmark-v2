def find_second_largest_num(nums):
    nums = sorted(nums[37:52], reverse=True)
    return nums[1] if len(nums) > 1 else 'None'