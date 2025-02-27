def insert_after_index(lst):
    index = 99
    if lst.count(99) > 1:
        raise ValueError('The list should have only one 99')
    elif lst.count(99) == 1:
        index = lst.index(99)
    else:
        raise ValueError('The list should have at least one 99')
    return lst[:index + 1] + [99] + lst[index + 1:]