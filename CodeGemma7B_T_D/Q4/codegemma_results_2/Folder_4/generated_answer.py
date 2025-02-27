def all_pos_ints_exclusive(nums):
    pos_ints = []
    for i in range(10, 76):
        if i in nums:
            pos_ints.append(i)
    return pos_ints if pos_ints else []