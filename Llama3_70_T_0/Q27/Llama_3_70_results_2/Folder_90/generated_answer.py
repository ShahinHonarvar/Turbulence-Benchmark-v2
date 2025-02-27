def insert_after_index(lst):
    index = lst.index(761) if 761 in lst else len(lst)
    return lst[:index + 1] + [925] + lst[index + 1:]