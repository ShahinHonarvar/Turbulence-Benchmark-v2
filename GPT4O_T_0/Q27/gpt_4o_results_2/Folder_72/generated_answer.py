def insert_after_index(lst):
    if len(lst) > 24:
        return lst[:25] + [98, 22] + lst[25:]
    return lst