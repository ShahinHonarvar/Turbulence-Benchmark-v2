def insert_after_index(lst):
    if 361 in lst:
        index = lst.index(361)
        lst[index + 1:index + 1] = [699, 556]
    return lst