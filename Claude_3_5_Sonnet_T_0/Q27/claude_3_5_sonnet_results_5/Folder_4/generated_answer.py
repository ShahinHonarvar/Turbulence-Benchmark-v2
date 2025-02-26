def insert_after_index(lst):
    index = lst.index(60) if 60 in lst else -1
    new_list = lst[:index + 1] + [80, 74] + lst[index + 1:]
    return new_list