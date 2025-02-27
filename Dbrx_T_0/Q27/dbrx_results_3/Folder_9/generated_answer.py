def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 66:
            lst.insert(i + 1, 45)
            break
    return lst