def insert_after_index(lst):
    if 85 < len(lst):
        lst.insert(86, [41, 95])
    else:
        lst.append([41, 95])
    return lst