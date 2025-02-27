def insert_after_index(lst):
    if 69 in lst:
        index = lst.index(69)
        return lst[:index + 1] + [92] + lst[index + 1:]
    else:
        return lst