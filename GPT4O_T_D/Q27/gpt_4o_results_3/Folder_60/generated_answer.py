def insert_after_index(lst):
    return lst[:22] + [74] + lst[22:] if len(lst) > 21 else lst + [74]