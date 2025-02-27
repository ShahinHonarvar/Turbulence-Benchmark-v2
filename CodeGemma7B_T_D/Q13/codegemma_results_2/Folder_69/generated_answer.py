def find_second_largest_num(nums):
    nums = sorted(nums[32:36])
    return nums[-2] if len(nums) >= 2 else 'None'