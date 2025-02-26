def insert_after_index(lst):
    target_index = 74
    if target_index < len(lst):
        return lst[:target_index + 1] + [49] + lst[target_index + 1:]
    else:
        return lst + [49]