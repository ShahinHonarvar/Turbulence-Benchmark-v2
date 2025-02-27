def find_second_largest_num(nums):
    if len(nums) < 52:
        return None
    nums = sorted(nums[29:52], reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]