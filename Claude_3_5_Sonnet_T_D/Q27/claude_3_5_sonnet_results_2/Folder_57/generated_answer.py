def insert_after_index(lst):
    if 90 in lst:
        index = lst.index(90)
        return lst[:index + 1] + [80] + lst[index + 1:]
    else:
        return lst