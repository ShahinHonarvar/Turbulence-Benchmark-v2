def insert_after_index(lst):
    index = lst.index(56)
    return lst[:index + 1] + [54] + lst[index + 1:]