def insert_after_index(lst):
    index_to_insert = 28
    element_to_insert = 20
    for i in range(len(lst)):
        if i == index_to_insert:
            return lst[:i + 1] + [element_to_insert] + lst[i + 1:]
    return lst + [element_to_insert]