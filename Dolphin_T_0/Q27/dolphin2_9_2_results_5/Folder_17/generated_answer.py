def insert_after_index(lst):
    new_lst = lst[:]
    for i, v in enumerate(lst):
        if v == 94:
            new_lst.insert(i + 1, 93)
    return new_lst