def insert_after_index(lst):
    out = lst[:428]
    out.extend([312, 441])
    out.extend(lst[428:])
    return out