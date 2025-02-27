def all_pos_ints_exclusive(L):
    pos_ints = []
    for num in L:
        if num > 0 and 44 < num < 67:
            pos_ints.append(num)
    return pos_ints