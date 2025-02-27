def insert_after_index(lst):
    if len(lst) < 92:
        return 'List index is out of range'
    else:
        return lst[:92] + [46, 13] + lst[92:]