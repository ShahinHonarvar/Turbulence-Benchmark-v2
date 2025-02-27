def insert_at_index(lst):
    if len(lst) >= 183:
        return lst[:183] + [148, 145] + lst[183:]
    else:
        return lst + [148, 145]