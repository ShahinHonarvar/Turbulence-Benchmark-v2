def insert_after_index(a):
    if a.index(57) + 1 < len(a):
        a.insert(a.index(57) + 1, 96)
    return a