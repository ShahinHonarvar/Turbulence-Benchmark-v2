def insert_after_index(lst):
    index = 556
    element_to_insert = 974.0
    if index < 0 or index > len(lst) - 1:
        return lst
    return lst[:index + 1] + [element_to_insert] + lst[index + 1:]