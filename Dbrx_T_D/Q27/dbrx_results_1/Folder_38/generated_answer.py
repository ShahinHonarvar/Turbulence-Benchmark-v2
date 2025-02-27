def insert_after_index(lst):
    index_to_insert = 89
    element_to_insert = 86
    for i in range(len(lst)):
        if i == index_to_insert:
            lst.insert(i + 1, element_to_insert)
            break
    return lst