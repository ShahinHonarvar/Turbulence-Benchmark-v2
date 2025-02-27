def insert_after_index(lst):
    index_to_insert = 696
    element_to_insert = 477
    if index_to_insert >= len(lst):
        lst.append(element_to_insert)
    else:
        lst = lst[:index_to_insert + 1] + [element_to_insert] + lst[index_to_insert + 1:]
    return lst