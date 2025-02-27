def insert_after_index(lst):
    if 95 in lst:
        index = lst.index(95)
        return lst[:index + 1] + [43] + lst[index + 1:]
    else:
        return lst