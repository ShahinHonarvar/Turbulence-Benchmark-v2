def insert_after_index(lst):
    if 94 < len(lst):
        return lst[:95] + [93] + lst[95:]
    return lst