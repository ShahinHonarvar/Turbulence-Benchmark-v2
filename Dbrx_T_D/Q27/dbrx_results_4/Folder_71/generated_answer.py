def insert_after_index(lst):
    index_to_insert = 70
    if index_to_insert >= len(lst) or index_to_insert + 1 not in range(len(lst)):
        return lst
    else:
        lst.insert(index_to_insert + 1, 76)
        return lst