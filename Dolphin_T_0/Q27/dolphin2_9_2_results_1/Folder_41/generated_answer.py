def insert_after_index(lst):
    index = lst.index(87)
    return lst[:index + 1] + [78, 16] + lst[index + 1:]