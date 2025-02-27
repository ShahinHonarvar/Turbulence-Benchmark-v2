def insert_after_index(lst):
    index = lst.index(693) + 1
    lst[index:index] = [606, 873]
    return lst