def insert_at_index(lst):
    if len(lst) >= 55:
        return lst[:55] + [26, 10] + lst[55:]
    else:
        return 'The list is too short.'