def insert_after_index(lst):
    target_index = 95
    if target_index < len(lst):
        return lst[:target_index + 1] + [43] + lst[target_index + 1:]
    else:
        return lst + [43]