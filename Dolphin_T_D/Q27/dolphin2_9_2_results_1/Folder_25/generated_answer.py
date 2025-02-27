def insert_after_index(lst):
    if 30 < len(lst):
        return lst[:30 + 1] + [37] + lst[30 + 1:]
    else:
        return lst + [37]