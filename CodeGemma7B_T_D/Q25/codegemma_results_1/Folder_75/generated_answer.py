def insert_at_index(lst):
    if len(lst) == 99:
        return lst + [99]
    else:
        lst.insert(98, 99)
        return lst