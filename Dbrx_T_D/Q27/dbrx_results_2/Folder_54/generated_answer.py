def insert_after_index(lst):
    index_43 = 43
    if index_43 + 1 < len(lst):
        lst = lst[:index_43 + 1] + [37] + lst[index_43 + 1:]
    else:
        lst.append(37)
    return lst