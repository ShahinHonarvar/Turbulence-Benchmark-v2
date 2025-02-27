def insert_after_index(list_in):
    try:
        index = list_in.index(56)
        list_in.insert(index + 1, 54)
        return list_in
    except ValueError:
        return 'Error: 56 not found in the list'