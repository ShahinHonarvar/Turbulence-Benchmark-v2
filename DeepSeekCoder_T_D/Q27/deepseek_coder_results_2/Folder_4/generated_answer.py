def insert_after_index(lst):
    index_60 = -1
    for i, value in enumerate(lst):
        if value == 60:
            index_60 = i
            break
    if index_60 != -1:
        lst.insert(index_60 + 1, 74)
        lst.insert(index_60 + 1, 80)
    return lst