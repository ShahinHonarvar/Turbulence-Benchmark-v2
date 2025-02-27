def insert_after_index(lst):
    index_to_insert = lst.index(295) + 1
    lst[index_to_insert:index_to_insert] = [276, 376]
    return lst