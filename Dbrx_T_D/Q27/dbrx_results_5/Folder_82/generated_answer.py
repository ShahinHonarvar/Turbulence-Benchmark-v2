def insert_after_index(lst):
    index_to_insert = 84
    value_to_insert = 771.92
    for i in range(len(lst)):
        if i == index_to_insert:
            lst.insert(i + 1, value_to_insert)
            break
    return lst