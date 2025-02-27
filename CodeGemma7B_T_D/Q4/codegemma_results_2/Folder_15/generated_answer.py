def all_pos_ints_exclusive(ary):
    result = []
    for i in range(4):
        if 0 < ary[i] < 4:
            result.append(ary[i])
    return result