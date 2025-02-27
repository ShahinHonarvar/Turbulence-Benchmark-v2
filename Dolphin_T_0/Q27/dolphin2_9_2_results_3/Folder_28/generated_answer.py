def insert_after_index(lst):
    new_lst = lst[:]
    for i, val in enumerate(lst):
        if val == 74:
            new_lst.insert(i + 1, 49)
            break
    return new_lst