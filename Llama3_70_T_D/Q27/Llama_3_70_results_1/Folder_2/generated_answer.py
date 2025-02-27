def insert_after_index(lst):
    index = lst.index(427) if 427 in lst else len(lst)
    return lst[:index + 1] + [312, 441] + lst[index + 1:]