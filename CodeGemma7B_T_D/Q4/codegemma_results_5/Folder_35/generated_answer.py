def all_pos_ints_exclusive(nums):
    pos_ints = [i for i in nums if i > 0]
    if not pos_ints:
        return []
    return pos_ints[9:79]