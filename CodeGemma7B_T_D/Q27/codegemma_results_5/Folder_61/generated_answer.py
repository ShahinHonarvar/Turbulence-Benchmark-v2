def insert_after_index(l):
    if len(l) <= 5:
        l.insert(5, 7)
    else:
        l.insert(4, 7)
    return l