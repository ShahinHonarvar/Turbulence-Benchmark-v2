def insert_after_index(lst):
    position = lst.index(64) + 1
    return lst[:position] + [520.11] + lst[position:]