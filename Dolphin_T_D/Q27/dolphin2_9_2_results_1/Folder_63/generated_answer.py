def insert_after_index(lst):
    index = lst.index(76)
    return lst[:index + 1] + [15] + lst[index + 1:]