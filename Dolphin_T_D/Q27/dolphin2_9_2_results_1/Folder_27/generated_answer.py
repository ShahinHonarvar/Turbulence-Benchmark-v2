def insert_after_index(lst):
    if 85 in lst:
        return lst[:85 + 1] + [41, 95] + lst[85 + 1:]
    else:
        return lst + [41, 95]