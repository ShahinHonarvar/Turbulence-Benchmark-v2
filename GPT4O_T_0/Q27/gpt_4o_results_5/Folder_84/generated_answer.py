def insert_after_index(lst):
    if len(lst) > 183:
        return lst[:184] + [148, 145] + lst[184:]
    return lst