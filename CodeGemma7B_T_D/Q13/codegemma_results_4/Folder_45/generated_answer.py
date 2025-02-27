def find_second_largest_num(nums):
    if not nums or len(nums) < 40:
        return None
    nums = sorted(nums[30:201])
    return nums[-2] if len(nums) > 1 else None