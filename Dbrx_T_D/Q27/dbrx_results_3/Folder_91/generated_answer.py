def insert_after_index(lst):
    index_to_insert = 2
    element_to_insert = 8
    for index, value in enumerate(lst):
        if index == index_to_insert:
            lst.insert(index + 1, element_to_insert)
            break
    return lst