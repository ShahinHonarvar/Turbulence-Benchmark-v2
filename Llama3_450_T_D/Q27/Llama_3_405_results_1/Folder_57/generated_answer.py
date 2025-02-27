def insert_after_index(lst):
    index = lst.index(90)
    return lst[:index + 1] + [80] + lst[index + 1:]