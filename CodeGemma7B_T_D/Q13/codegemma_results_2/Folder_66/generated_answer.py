def find_second_largest_num(nums):
    if not nums or len(nums) < 6:
        return None
    nums = nums[50:55]
    nums.sort(reverse=True)
    return nums[1] if len(nums) > 1 else None