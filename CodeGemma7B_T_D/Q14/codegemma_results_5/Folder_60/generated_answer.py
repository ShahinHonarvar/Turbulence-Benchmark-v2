def find_second_smallest_num(nums):
    nums = sorted(nums)
    if len(nums) > 56 and len(nums) <= 98:
        return nums[56]
    elif len(nums) > 98:
        return nums[98]
    else:
        return 'None'