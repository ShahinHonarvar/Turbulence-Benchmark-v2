def all_pos_ints_inclusive(nums):
    if not nums:
        return []
    pos_nums = [n for n in nums if n > 0]
    if not pos_nums:
        return []
    return pos_nums[74:86]