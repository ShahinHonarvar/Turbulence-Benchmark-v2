def insert_after_index(lst):
    target_index = 564
    if target_index < len(lst):
        return lst[:target_index + 1] + [149] + lst[target_index + 1:]
    else:
        return lst + [149]