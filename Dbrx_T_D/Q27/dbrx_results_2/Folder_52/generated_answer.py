def insert_after_index(lst):
    index_to_insert = 97
    if index_to_insert < 0 or index_to_insert >= len(lst):
        return lst
    new_lst = lst[:index_to_insert + 1] + [72.27] + lst[index_to_insert + 1:]
    return new_lst