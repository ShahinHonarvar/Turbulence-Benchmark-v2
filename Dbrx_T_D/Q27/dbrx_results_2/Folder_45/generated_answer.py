def insert_after_index(lst):
    index_to_insert = -1
    for i in range(len(lst)):
        if lst[i] == 84:
            index_to_insert = i + 1
            break
    if index_to_insert != -1:
        lst.insert(index_to_insert, [13, 46])
    return lst