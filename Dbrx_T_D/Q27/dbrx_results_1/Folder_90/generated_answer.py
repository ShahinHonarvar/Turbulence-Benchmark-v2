def insert_after_index(lst):
    idx = 761
    element_to_add = 925
    if idx < 0 or idx >= len(lst):
        return lst
    return lst[:idx + 1] + [element_to_add] + lst[idx + 1:]