def insert_after_index(lst):
    if 99 in lst:
        index = lst.index(99)
        return lst[:index + 1] + [99] + lst[index + 1:]
    else:
        return lst