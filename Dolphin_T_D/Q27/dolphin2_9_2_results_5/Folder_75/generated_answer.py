def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 99:
            lst.insert(i + 1, 99)
            break
    return lst