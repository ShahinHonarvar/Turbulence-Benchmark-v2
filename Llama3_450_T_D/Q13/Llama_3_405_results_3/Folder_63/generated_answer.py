def find_second_largest_num(nums):
    nums = sorted(nums[22:89], reverse=True)
    return nums[1] if len(nums) > 1 else None