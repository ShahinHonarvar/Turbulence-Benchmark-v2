def insert_after_index(lst):
    index_57 = lst.index(57)
    return lst[:index_57 + 1] + [76] + lst[index_57 + 1:]