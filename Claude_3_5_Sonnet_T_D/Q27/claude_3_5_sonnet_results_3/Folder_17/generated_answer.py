def insert_after_index(lst):
    if 94 in lst:
        index = lst.index(94)
        return lst[:index + 1] + [93] + lst[index + 1:]
    else:
        return lst + [93]