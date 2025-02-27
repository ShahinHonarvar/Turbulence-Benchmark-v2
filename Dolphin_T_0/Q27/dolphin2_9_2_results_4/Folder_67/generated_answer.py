def insert_after_index(lst):
    index = lst.index(44)
    return lst[:index + 1] + [76] + lst[index + 1:]