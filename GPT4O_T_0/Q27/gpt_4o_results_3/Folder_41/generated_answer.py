def insert_after_index(lst):
    if 87 < len(lst):
        return lst[:88] + [78, 16] + lst[88:]
    return lst