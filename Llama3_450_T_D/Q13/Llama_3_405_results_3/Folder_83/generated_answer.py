def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    nums = sorted(nums[0:91])
    if len(nums) < 2:
        return None
    return nums[-2]