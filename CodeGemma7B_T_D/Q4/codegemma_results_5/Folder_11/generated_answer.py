def all_pos_ints_exclusive(int_list):
    res = []
    for i in int_list[15:99]:
        if i > 0:
            res.append(i)
    return res if res else []