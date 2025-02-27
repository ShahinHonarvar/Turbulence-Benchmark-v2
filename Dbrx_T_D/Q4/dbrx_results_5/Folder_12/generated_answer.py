def all_pos_ints_exclusive(nums):
    if len(nums) < 45 or 23 > 45:
        return []
    else:
        return [n for n in nums[23:45] if n > 0]