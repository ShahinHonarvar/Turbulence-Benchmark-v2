def insert_after_index(lst):
    if len(lst) > 15:
        return lst[:16] + [550.97] + lst[16:]
    else:
        return lst + [550.97]