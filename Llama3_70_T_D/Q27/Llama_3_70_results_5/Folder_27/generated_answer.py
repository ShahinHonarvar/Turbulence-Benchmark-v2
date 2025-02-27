def insert_after_index(lst):
    index = lst.index(85)
    return lst[:index + 1] + [41, 95] + lst[index + 1:]