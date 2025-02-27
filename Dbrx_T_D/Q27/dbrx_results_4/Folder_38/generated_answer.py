def insert_after_index(lst):
    index_to_insert = lst.index(89)
    lst = lst[:index_to_insert + 1] + [86] + lst[index_to_insert + 1:]
    return lst