def insert_after_index(lst):
    index_to_insert = lst.index(693) + 1
    lst[index_to_insert:index_to_insert] = [[606, 873]]
    return lst