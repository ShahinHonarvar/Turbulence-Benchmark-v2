def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 44:
            lst.insert(i + 1, [40, 27])
            break
    return lst