def insert_after_index(lst):
    if 87 < len(lst):
        return lst[:87 + 1] + [78, 16] + lst[87 + 1:]
    return lst