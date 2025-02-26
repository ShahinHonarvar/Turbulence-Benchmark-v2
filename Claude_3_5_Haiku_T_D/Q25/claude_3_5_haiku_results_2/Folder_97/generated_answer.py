def insert_at_index(lst):
    if len(lst) <= 500:
        return lst + [912, 170]
    result = lst.copy()
    result.insert(500, 912)
    result.insert(501, 170)
    return result