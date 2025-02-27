def all_pos_ints_exclusive(nums):
    if len(nums) < 7:
        return []
    else:
        return [num for num in nums[1:6] if num > 0]