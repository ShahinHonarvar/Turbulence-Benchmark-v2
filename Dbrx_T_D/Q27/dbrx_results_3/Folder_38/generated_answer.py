def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 89:
            lst.insert(i + 1, 86)
    return lst