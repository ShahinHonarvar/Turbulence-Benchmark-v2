def insert_after_index(lst):
    if 28 in range(len(lst)):
        return lst[:29] + [20] + lst[29:]
    else:
        return 'Index 28 is out of range'