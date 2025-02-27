def all_pos_ints_exclusive(nums):
    if len(nums) <= 50:
        return []
    return [num for num in nums[50:74] if num > 0]