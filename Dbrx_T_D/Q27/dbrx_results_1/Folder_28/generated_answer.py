def insert_after_index(lst):
    if 74 in lst:
        index = lst.index(74) + 1
        lst = lst[:index] + [49] + lst[index:]
    return lst