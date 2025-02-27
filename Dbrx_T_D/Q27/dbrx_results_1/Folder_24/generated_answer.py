def insert_after_index(lst):
    index_42 = lst.index(42)
    return lst[:index_42 + 1] + [53] + lst[index_42 + 1:]