def insert_after_index(lst):
    if len(lst) > 564:
        return lst[:565] + [149] + lst[565:]
    return lst + [149] if len(lst) == 564 else lst