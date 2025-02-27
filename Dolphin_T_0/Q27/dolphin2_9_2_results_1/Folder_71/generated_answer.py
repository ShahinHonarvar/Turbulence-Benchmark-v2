def insert_after_index(lst):
    index_70 = lst.index(70)
    return lst[:index_70 + 1] + [76] + lst[index_70 + 1:]