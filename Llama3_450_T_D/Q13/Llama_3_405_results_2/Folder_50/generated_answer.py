def find_second_largest_num(nums):
    if len(nums) < 85:
        return None
    nums = sorted(nums[70:85], reverse=True)
    return nums[1] if nums[1] != nums[0] and len(nums) > 1 else None