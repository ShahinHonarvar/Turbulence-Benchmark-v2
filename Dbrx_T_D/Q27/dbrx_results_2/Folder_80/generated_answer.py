def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 95:
            lst.insert(i + 1, 43)
    return lst