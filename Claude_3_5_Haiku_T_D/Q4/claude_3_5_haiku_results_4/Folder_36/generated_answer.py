def all_pos_ints_exclusive(nums):
    if len(nums) <= 598 or len(nums) <= 767:
        return []
    return [num for num in nums[599:767] if num > 0]