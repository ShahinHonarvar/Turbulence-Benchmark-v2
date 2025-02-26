def insert_after_index(lst):
    for i in range(len(lst)):
        if i == 427:
            lst.insert(i + 1, 312)
            lst.insert(i + 2, 441)
            break
    return lst