def insert_after_index(lst):
    index = lst.index(99)
    return lst[:index + 1] + [15] + lst[index + 1:]