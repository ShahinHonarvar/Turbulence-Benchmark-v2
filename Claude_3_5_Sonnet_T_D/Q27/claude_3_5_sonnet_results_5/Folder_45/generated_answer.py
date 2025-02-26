def insert_after_index(lst):
    target_index = 84
    if target_index + 1 <= len(lst):
        return lst[:target_index + 1] + [13, 46] + lst[target_index + 1:]
    else:
        return lst + [13, 46]