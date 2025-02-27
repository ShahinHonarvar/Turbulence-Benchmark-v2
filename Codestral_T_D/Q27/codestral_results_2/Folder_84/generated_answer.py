def insert_after_index(lst):
    index = lst.index(183)
    lst[index + 1:index + 1] = [148, 145]
    return lst