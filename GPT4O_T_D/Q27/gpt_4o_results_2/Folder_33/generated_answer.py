def insert_after_index(lst):
    if len(lst) > 556:
        return lst[:557] + [974.0] + lst[557:]
    return lst + [974.0]