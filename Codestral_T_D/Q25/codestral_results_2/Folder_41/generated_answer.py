def insert_at_index(lst):
    if len(lst) > 87:
        lst.insert(87, [78, 16])
    else:
        lst.append([78, 16])
    return lst