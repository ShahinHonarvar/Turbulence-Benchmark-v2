def insert_at_index(lst, index=89):
    if not isinstance(lst, list):
        raise ValueError('First argument must be a list')
    if not isinstance(index, int):
        raise ValueError('Index must be an integer')
    if index < 0:
        raise ValueError('Index must be positive')
    return lst[:index] + [86] + lst[index:]