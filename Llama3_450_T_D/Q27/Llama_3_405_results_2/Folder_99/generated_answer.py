def insert_after_index(lst):
    if len(lst) <= 295:
        return lst + [276, 376]
    else:
        return lst[:295] + [lst[295], 276, 376] + lst[296:]