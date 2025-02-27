def find_largest_num(nums):
    if len(nums) < 2:
        return max(nums)
    return max(nums[0], nums[1])