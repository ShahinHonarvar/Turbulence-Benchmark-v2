def insert_after_index(lst):
    for i, n in enumerate(lst):
        if n == 99:
            lst.insert(i + 1, 99)
            return lst
    else:
        lst.append(99)
    return lst