def insert_after_index(lst):
    index_to_insert = lst.index(44) + 1
    new_element = [40, 27]
    lst = lst[:index_to_insert] + [new_element] + lst[index_to_insert:]
    return lst