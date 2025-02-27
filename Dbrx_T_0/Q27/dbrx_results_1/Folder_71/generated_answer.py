def insert_after_index(lst):
    index_to_insert = 70
    for i in range(len(lst)):
        if i == index_to_insert:
            lst.insert(i + 1, 76)
            break
    return lst