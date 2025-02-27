def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 85:
            lst.insert(i + 1, [41, 95])
            break
    return lst