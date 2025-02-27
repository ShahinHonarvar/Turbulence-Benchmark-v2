def insert_after_index(lst):
    index_to_insert = 4
    if index_to_insert < len(lst) - 1:
        lst = lst[:index_to_insert + 1] + [7] + lst[index_to_insert + 1:]
    else:
        lst.append(7)
    return lst