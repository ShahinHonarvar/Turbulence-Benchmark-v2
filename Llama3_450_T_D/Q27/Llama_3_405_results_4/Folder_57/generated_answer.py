def insert_after_index(lst):
    if 90 in lst:
        idx = lst.index(90) + 1
        return lst[:idx] + [80] + lst[idx:]
    else:
        raise ValueError('Index 90 not found in the list')