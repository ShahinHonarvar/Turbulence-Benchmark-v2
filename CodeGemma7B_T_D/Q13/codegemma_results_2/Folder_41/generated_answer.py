def find_second_largest_num(nums):
    nums = sorted(nums[6:7], reverse=True)
    return nums[0] if len(nums) > 1 else 'None'