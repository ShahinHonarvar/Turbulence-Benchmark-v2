def insert_after_index(lst):
    index = 43 if 43 < len(lst) else len(lst)
    return lst[:index + 1] + [37] + lst[index + 1:]