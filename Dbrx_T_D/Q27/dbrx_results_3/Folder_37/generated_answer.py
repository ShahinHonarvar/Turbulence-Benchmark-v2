def insert_after_index(lst):
    index_to_insert = 35
    for i, item in enumerate(lst):
        if i == index_to_insert:
            index_to_insert += 1
        if i == index_to_insert:
            lst.insert(i, 88)
            break
    return lst