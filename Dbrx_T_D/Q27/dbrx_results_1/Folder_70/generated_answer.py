def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 412:
            lst.insert(i + 1, 668)
            break
    return lst