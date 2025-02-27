def find_second_largest_num(nums):
    nums = sorted(nums[22:64])
    return nums[-2] if len(nums) > 1 else 'None'