def insert_after_index(lst):
    index = lst.index(983)
    lst = lst[:index + 1] + [369] + lst[index + 1:]
    return lst