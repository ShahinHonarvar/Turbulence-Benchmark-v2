def insert_after_index(lst):
    if 74 in lst:
        index = lst.index(74)
        return lst[:index + 1] + [49] + lst[index + 1:]
    else:
        return lst