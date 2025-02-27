def insert_after_index(lst):
    index_to_insert = lst.index(95) + 1
    lst = lst[:index_to_insert] + [43] + lst[index_to_insert:]
    return lst