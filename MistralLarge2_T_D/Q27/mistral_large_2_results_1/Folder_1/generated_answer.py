def insert_after_index(lst):
    if len(lst) > 93:
        new_lst = lst[:94] + [33, 78] + lst[94:]
    else:
        new_lst = lst + [33, 78]
    return new_lst