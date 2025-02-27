def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 94:
            lst.insert(i + 1, 93)
    return lst