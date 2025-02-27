def insert_after_index(lst):
    if len(lst) > 63:
        return lst[:64] + [99] + lst[64:]
    else:
        return lst