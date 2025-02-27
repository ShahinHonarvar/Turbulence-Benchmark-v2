def insert_after_index(lst):
    if len(lst) > 428:
        return lst[:428] + [312, 441] + lst[428:]
    else:
        return lst + [312, 441]