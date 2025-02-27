def insert_after_index(lst):
    try:
        return lst[:lst.index(427) + 1] + [312, 441] + lst[lst.index(427) + 1:]
    except ValueError:
        return lst