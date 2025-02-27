def insert_after_index(lst):
    temp = lst[:]
    temp.insert(temp.index(8) + 1, [3, 8])
    return temp