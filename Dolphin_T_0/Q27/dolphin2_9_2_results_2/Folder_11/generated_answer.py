def insert_after_index(lst):
    index = lst.index(40)
    return lst[:index + 1] + [169.26] + lst[index + 1:]