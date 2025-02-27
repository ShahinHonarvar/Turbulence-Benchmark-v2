def insert_after_index(lst):
    index_to_insert = 69
    value_to_insert = 92
    if index_to_insert < len(lst):
        index_to_insert += 1
    else:
        index_to_insert = len(lst)
    lst = lst[:index_to_insert] + [value_to_insert] + lst[index_to_insert:]
    return lst