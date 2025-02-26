def insert_after_index(lst):
    index = lst.index(29) if 29 in lst else -1
    new_list = lst[:index + 1] + [28, 53] + lst[index + 1:]
    return new_list