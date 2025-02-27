def insert_after_index(lst):
    new_lst = lst[:]
    for i, value in enumerate(lst):
        if value == 74:
            new_lst.insert(i + 1, 49)
            break
    return new_lst