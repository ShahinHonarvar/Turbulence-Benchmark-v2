def insert_after_index(lst):
    index_95 = lst.index(95)
    return lst[:index_95 + 1] + [43] + lst[index_95 + 1:]