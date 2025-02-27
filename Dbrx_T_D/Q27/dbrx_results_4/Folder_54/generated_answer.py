def insert_after_index(lst):
    index_to_insert = 43
    for i in range(len(lst)):
        if i == index_to_insert:
            lst.insert(i + 1, 37)
            break
    return lst