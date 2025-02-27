def insert_after_index(lst):
    if len(lst) > 60:
        return lst[:61] + [80, 74] + lst[61:]
    else:
        return lst + [80, 74]