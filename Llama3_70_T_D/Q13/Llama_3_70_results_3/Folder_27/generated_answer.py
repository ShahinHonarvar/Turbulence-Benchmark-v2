def find_second_largest_num(nums):
    if len(nums) < 94:
        return None
    nums = sorted(nums[66:94])
    if len(nums) < 2:
        return None
    return nums[-2]