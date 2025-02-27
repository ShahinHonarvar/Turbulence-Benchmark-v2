def insert_at_index(lst):
    lst.append(None)
    for i in range(len(lst) - 1, 52, -1):
        lst[i] = lst[i - 1]
    lst[52] = 38
    return lst