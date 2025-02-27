def insert_after_index(lst):
    index_44 = lst.index(44)
    return lst[:index_44 + 1] + [76] + lst[index_44 + 1:]