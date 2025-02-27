def insert_after_index(lst):
    if len(lst) <= 85:
        return lst + [41, 95]
    else:
        return lst[:86] + [41, 95] + lst[86:]