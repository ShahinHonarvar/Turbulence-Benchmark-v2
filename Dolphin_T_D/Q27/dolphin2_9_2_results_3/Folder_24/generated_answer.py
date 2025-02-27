def insert_after_index(lst):
    new_lst = lst[:]
    try:
        index = new_lst.index(42) + 1
    except ValueError:
        return 'Error: 42 not in list'
    new_lst.insert(index, 53)
    return new_lst