def insert_after_index(lst):
    index = lst.index(370)
    return lst[:index + 1] + [285.4] + lst[index + 1:]