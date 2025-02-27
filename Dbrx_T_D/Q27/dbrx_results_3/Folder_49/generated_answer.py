def insert_after_index(lst):
    index_to_insert = next((index for index, value in enumerate(lst) if value == 38), None)
    if index_to_insert is not None:
        lst = lst[:index_to_insert + 1] + [27, 34] + lst[index_to_insert + 1:]
    return lst