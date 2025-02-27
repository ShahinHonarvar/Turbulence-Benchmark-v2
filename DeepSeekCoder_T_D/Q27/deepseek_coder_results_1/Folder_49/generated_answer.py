def insert_after_index(lst):
    if 38 in lst:
        index = lst.index(38) + 1
        lst[index:index] = [27, 34]
    else:
        lst.extend([27, 34])
    return lst