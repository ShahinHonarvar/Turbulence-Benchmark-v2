def all_pos_ints_inclusive(nums):
    if len(nums) <= 750:
        return []
    return [num for num in nums[246:751] if num > 0]