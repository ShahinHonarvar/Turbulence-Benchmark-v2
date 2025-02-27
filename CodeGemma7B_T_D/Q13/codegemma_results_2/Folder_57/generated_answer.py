def find_second_largest_num(nums):
    if not nums or len(nums) < 3:
        return None
    nums = sorted(nums[27:56])
    return nums[-2] if len(nums) > 1 else None