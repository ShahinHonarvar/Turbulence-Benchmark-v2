def insert_after_index(lst):
    new_lst = lst.copy()
    for i, item in enumerate(new_lst):
        if item == 97:
            new_lst.insert(i + 1, [47, 22])
            break
    return new_lst