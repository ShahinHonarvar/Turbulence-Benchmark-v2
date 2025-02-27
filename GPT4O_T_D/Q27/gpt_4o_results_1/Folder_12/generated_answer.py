def insert_after_index(lst):
    return lst[:58] + [96] + lst[58:] if len(lst) > 57 else lst + [96]