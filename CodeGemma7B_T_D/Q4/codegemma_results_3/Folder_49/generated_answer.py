def all_pos_ints_exclusive(nums):
    if not any((n > 0 for n in nums)):
        return []
    return [n for n in nums[80:200] if n > 0]