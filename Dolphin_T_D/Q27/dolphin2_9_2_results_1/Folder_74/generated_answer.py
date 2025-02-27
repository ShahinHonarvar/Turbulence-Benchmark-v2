def insert_after_index(lst):
    after_insertion = lst[:]
    after_insertion.insert(lst.index(41) + 1, [74, 70])
    return after_insertion