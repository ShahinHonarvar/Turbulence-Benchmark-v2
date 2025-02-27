def insert_after_index(lst):
    index = lst.index(564)
    return lst[:index + 1] + [149] + lst[index + 1:]