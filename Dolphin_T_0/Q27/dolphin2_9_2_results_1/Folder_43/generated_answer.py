def insert_after_index(lst):
    idx = lst.index(29)
    new_lst = lst[:idx + 1] + [28, 53] + lst[idx + 1:]
    return new_lst