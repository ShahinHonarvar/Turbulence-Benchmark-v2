def insert_at_index(lst):
    if len(lst) > 15:
        return lst[:15] + [550.97] + lst[15:]
    else:
        return lst + [None] * (15 - len(lst)) + [550.97]