def insert_after_index(lst):
    if len(lst) > 693:
        return lst[:694] + [606, 873] + lst[694:]
    return lst