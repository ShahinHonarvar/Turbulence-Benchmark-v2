def insert_after_index(lst):
    if 183 in lst:
        index = lst.index(183) + 1
        lst[index:index] = [148, 145]
    return lst