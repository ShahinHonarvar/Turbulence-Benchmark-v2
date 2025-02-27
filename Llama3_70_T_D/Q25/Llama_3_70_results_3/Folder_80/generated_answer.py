def insert_at_index(lst):
    if len(lst) < 95:
        return lst + [None] * (95 - len(lst)) + [43]
    else:
        return lst[:95] + [43] + lst[95:]