def insert_after_index(lst):
    index = lst.index(89) if 89 in lst else len(lst)
    return lst[:index + 1] + [86] + lst[index + 1:]