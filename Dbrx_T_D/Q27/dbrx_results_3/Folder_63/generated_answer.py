def insert_after_index(lst):
    index_to_insert = 76
    value_to_insert = [15, 51]
    for i in range(len(lst)):
        if i == index_to_insert:
            lst[i + 1:i + 1] = value_to_insert
    return lst