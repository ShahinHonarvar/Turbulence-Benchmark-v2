def find_second_largest_num(nums):
    nums = sorted(nums[74:96])[::-1]
    return nums[1] if len(nums) > 1 else 'None'