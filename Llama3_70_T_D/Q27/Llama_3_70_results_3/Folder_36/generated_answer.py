def insert_after_index(lst):
    if len(lst) > 361:
        return lst[:362] + [699, 556] + lst[362:]
    else:
        return lst + [699, 556]