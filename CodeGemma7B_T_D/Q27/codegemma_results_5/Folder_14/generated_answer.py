def insert_after_index(lst):
    if len(lst) <= 15:
        return 'Error: Index out of bounds.'
    else:
        lst.insert(16, 550.97)
        return lst