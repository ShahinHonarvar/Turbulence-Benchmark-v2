def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 96:
            lst.insert(i + 1, 36)
            break
    return lst