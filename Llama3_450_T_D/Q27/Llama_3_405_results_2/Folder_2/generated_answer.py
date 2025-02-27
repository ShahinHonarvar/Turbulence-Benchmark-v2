def insert_after_index(lst):
    if len(lst) <= 427:
        return lst + [312, 441]
    else:
        return lst[:428] + [312, 441] + lst[428:]