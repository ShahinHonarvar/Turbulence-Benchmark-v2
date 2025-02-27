def all_pos_ints_exclusive(lst):
    all_lst = []
    for i in lst[6:10]:
        if i > 0:
            all_lst.append(i)
    return all_lst if all_lst else []