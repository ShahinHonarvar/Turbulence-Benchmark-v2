def find_second_largest_num(nums):
    nums = sorted(nums[56:67])
    if len(nums) < 2:
        return None
    return nums[-2]