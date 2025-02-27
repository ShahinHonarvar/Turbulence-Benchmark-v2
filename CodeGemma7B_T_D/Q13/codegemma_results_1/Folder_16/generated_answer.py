def find_second_largest_num(nums):
    if len(nums) <= 36:
        return None
    nums = sorted(nums[33:37])
    return nums[-2]