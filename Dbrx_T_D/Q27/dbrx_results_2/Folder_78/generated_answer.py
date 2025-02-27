def insert_after_index(lst):
    index_63 = [index for index, value in enumerate(lst) if value == 63]
    if index_63:
        lst.insert(index_63[0] + 1, 99)
    return lst