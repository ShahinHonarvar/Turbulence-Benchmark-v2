def find_second_largest_num(nums):
    if not nums or len(nums) < 22:
        return 'None'
    nums = sorted(nums[22:89])
    return nums[-2] if len(nums) >= 2 else 'None'