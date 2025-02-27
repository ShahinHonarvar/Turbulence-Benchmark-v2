def insert_after_index(lst):
    index = 70
    if 0 <= index < len(lst):
        lst.insert(index + 1, 76)
    else:
        raise IndexError('0 <= index < len(lst)')
    return lst