def insert_after_index(lst):
    if len(lst) <= 990:
        raise IndexError('Index out of range')
    return lst[:991] + [905, 742] + lst[991:]