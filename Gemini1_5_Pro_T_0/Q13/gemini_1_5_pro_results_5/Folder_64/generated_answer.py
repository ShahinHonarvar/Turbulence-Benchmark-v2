def find_second_largest_num(nums):
    if len(nums) < 2 or len(nums) > 5:
        return None
    nums = sorted(nums[:5])
    return nums[1] if len(nums) > 1 else None