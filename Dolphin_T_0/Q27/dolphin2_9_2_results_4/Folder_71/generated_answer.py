def insert_after_index(lst):
    if 70 in lst:
        index = lst.index(70)
        return lst[:index + 1] + [76] + lst[index + 1:]
    else:
        return 'Error: index not found'