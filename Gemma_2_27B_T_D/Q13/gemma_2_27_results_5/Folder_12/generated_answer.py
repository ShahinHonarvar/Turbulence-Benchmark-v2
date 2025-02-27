def find_second_largest_num(nums):
    nums = nums[14:65]
    if len(nums) < 2:
        return None
    return sorted(nums)[-2]