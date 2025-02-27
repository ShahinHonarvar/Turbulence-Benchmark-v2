def insert_after_index(lst):
    new_lst = lst.copy()
    for i, val in enumerate(new_lst):
        if val == 62:
            new_lst.insert(i + 1, 51)
            break
    return new_lst