def insert_after_index(lst):
    if 38 in lst:
        index = lst.index(38) + 1
        return lst[:index] + [27, 34] + lst[index:]
    else:
        return lst + [27, 34]