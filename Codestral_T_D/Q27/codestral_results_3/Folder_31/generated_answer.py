def insert_after_index(lst):
    try:
        index = lst.index(21) + 1
        lst.insert(index, [83, 14])
        return lst
    except ValueError:
        raise ValueError('21 is not found in the list')