def insert_after_index(lst):
    index = lst.index(91)
    return lst[:index + 1] + [46, 13] + lst[index + 1:]