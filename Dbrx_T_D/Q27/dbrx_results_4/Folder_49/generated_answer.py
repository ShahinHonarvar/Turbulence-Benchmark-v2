def insert_after_index(lst):
    index_to_insert = next((i for i, x in enumerate(lst) if x == 38), None)
    if index_to_insert is not None:
        lst = lst[:index_to_insert + 1] + [27, 34] + lst[index_to_insert + 1:]
    return lst