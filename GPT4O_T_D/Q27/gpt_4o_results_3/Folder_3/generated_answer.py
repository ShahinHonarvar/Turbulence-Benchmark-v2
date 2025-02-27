def insert_after_index(lst):
    if len(lst) > 31:
        return lst[:32] + [88, 51] + lst[32:]
    return lst