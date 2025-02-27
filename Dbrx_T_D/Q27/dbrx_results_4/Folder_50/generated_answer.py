def insert_after_index(lst):
    index_52 = lst.index(52)
    return lst[:index_52 + 1] + [38] + lst[index_52 + 1:]