def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 41:
            lst.insert(i + 1, [74, 70])
    return lst