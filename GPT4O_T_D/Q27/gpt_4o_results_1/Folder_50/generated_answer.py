def insert_after_index(lst):
    return lst[:53] + [38] + lst[53:] if len(lst) > 52 else lst + [38]