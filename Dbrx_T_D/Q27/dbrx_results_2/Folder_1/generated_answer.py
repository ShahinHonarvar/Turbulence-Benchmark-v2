def insert_after_index(lst):
    index_to_insert = lst.index(93) + 1
    return lst[:index_to_insert] + [33, 78] + lst[index_to_insert:]