def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 90:
            lst.insert(i + 1, 80)
            return lst
    return lst + [80]