def insert_after_index(lst):
    index = lst.index(94)
    return lst[:index + 1] + [93] + lst[index + 1:]