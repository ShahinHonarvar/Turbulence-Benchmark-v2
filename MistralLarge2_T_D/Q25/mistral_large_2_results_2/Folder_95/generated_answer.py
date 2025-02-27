def insert_at_index(lst):
    if len(lst) < 20:
        return lst[:20] + [80] + lst[20:]
    else:
        return lst[:20] + [80] + lst[20:]