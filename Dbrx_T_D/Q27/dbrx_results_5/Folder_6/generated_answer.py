def insert_after_index(lst):
    index_to_insert = 86
    element_to_insert = 581.49
    if index_to_insert < len(lst) - 1:
        return lst[:index_to_insert + 1] + [element_to_insert] + lst[index_to_insert + 1:]
    else:
        return lst[:index_to_insert + 1] + [element_to_insert]