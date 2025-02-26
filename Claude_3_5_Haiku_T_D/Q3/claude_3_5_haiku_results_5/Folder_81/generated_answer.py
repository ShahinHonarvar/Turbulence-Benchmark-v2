def all_pos_ints_inclusive(nums):
    if len(nums) <= 100:
        return []
    return [num for num in nums[10:101] if num > 0]