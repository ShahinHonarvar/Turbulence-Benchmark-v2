def insert_after_index(lst):
    index_to_insert = next((i for i, x in enumerate(lst) if x == 35), None)
    if index_to_insert is not None:
        return lst[:index_to_insert + 1] + [90, 76] + lst[index_to_insert + 1:]
    else:
        return lst