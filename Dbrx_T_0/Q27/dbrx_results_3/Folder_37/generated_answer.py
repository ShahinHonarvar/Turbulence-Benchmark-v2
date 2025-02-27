def insert_after_index(lst):
    index_to_insert = 35
    for i in range(len(lst)):
        if i == index_to_insert:
            lst.insert(i + 1, 88)
            break
    return lst