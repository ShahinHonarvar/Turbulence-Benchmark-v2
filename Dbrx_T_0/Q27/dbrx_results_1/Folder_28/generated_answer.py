def insert_after_index(lst):
    index_to_insert = 74
    element_to_insert = 49
    if index_to_insert < 0 or index_to_insert >= len(lst) - 1:
        return lst
    new_lst = lst[:index_to_insert + 1] + [element_to_insert] + lst[index_to_insert + 1:]
    return new_lst