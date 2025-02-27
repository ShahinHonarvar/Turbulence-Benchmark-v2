def insert_after_index(lst):
    index = lst.index(85)
    new_lst = lst[:index + 1] + [27] + lst[index + 1:]
    return new_lst