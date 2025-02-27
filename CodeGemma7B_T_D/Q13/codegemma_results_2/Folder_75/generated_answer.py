def find_second_largest_num(nums):
    nums = sorted(nums[56:58], reverse=True)
    return nums[0] if len(nums) >= 2 else 'None'