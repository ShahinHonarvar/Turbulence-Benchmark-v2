def insert_after_index(lst):
    if len(lst) > 76:
        return lst[:77] + [15, 51] + lst[77:]
    return lst