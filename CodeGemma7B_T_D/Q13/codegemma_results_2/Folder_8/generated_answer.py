def find_second_largest_num(nums):
    if not nums or len(nums) < 24:
        return None
    nums = nums[23:24]
    return sorted(nums)[-2]