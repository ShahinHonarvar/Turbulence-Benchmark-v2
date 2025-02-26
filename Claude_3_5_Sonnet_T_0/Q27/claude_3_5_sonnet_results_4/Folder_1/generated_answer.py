def insert_after_index(lst):
    index = lst.index(93) if 93 in lst else -1
    new_list = lst[:index + 1] + [33, 78] + lst[index + 1:]
    return new_list