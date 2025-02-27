def insert_after_index(lst):
    if 89 in lst:
        index = lst.index(89)
        return lst[:index + 1] + [86] + lst[index + 1:]
    else:
        return lst + [86]