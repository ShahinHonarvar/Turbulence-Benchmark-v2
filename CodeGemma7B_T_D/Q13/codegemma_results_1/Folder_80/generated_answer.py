def find_second_largest_num(nums):
    if len(nums) < 64 or len(nums) > 67:
        return None
    nums.sort(reverse=True)
    if nums[65] == nums[66]:
        return None
    return nums[65]