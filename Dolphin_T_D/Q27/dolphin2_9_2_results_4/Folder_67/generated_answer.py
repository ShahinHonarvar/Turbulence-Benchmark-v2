def insert_after_index(lst):
    for index, value in enumerate(lst):
        if value == 44:
            index_after_44 = index + 1
        lst.insert(index_after_44, 76)
        break
    return lst