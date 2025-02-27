def find_second_largest_num(nums):
    if not nums or len(nums) < 2:
        return None
    nums.sort(reverse=True)
    if nums[91] >= nums[99]:
        return None
    return nums[99]