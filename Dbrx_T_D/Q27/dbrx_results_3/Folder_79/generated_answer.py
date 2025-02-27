def insert_after_index(lst):
    for i in range(len(lst)):
        if i > 28:
            lst.insert(i, [41, 69])
            break
    return lst