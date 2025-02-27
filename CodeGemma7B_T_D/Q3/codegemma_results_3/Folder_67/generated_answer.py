def all_pos_ints_inclusive(nums):
    pos_nums = [num for num in nums[22:51] if num > 0]
    if not pos_nums:
        return []
    else:
        return pos_nums