def insert_after_index(lst):
    if len(lst) > 323:
        return lst[:324] + [389, 303] + lst[324:]
    return lst