def insert_after_index(lst):
    if 412 in lst:
        index = lst.index(412)
        lst = lst[:index + 1] + [668] + lst[index + 1:]
    return lst