def insert_after_index(lst):
    index = None
    for i, val in enumerate(lst):
        if val == 983:
            index = i
            break
    if index is None:
        raise ValueError('No element with value 983 found in the list')
    return lst[:index + 1] + [369] + lst[index + 1:]