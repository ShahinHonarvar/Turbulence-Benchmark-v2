def insert_after_index(lst):
    index_to_insert = next((index for index, value in enumerate(lst) if value == 74), None)
    if index_to_insert is not None:
        return lst[:index_to_insert + 1] + [51, 29] + lst[index_to_insert + 1:]
    else:
        return lst