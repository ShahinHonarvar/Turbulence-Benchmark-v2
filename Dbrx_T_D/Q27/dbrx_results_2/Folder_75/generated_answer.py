def insert_after_index(lst):
    index = lst.index(99)
    lst = lst[:index + 1] + [99] + lst[index + 1:]
    return lst