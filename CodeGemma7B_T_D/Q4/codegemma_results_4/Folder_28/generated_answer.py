def all_pos_ints_exclusive(nums):
    lst = []
    for i in range(20, 52):
        if i not in nums and i > 0:
            lst.append(i)
    return lst