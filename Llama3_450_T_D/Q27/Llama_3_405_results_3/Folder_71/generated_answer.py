def insert_after_index(lst):
    if 70 in lst:
        return lst[:lst.index(70) + 1] + [76] + lst[lst.index(70) + 1:]
    else:
        return lst