def insert_after_index(lst):
    if 74 < len(lst):
        return lst[:75] + [51, 29] + lst[75:]
    else:
        return lst + [0] * (75 - len(lst) - 1) + [51, 29]