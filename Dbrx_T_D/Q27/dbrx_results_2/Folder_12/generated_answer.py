def insert_after_index(lst):
    index_to_insert = 57
    for i in range(len(lst)):
        if i == index_to_insert + 1:
            lst.insert(i, 96)
            break
    return lst