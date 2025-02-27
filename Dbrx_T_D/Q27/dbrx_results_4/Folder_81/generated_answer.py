def insert_after_index(lst):
    index_to_insert = 28
    for i, item in enumerate(lst):
        if i == index_to_insert:
            lst.insert(i + 1, 20)
            break
    return lst