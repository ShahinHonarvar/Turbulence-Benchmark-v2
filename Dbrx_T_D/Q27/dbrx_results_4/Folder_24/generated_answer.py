def insert_after_index(lst):
    index_to_insert = 42
    if index_to_insert >= len(lst):
        lst.append(53)
    else:
        lst = lst[:index_to_insert + 1] + [53] + lst[index_to_insert + 1:]
    return lst