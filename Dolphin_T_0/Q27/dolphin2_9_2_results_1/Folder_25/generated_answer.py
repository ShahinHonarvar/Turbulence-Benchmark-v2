def insert_after_index(lst):
    new_lst = lst.copy()
    if 30 in new_lst:
        new_lst.insert(new_lst.index(30) + 1, 37)
    else:
        new_lst.append(37)
    return new_lst