def insert_after_index(lst):
    index = lst.index(89)
    return lst[:index + 1] + [86] + lst[index + 1:]