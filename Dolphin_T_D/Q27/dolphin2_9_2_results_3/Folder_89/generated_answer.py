def insert_after_index(lst):
    new_lst = lst[:]
    for i, e in enumerate(new_lst):
        if e == 62:
            new_lst.insert(i + 1, 51)
            break
    return new_lst