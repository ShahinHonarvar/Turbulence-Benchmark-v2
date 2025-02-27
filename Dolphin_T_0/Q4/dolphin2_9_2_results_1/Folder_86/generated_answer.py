def all_pos_ints_exclusive(integers):
    result = [i for i in integers[18:60] if i > 0]
    if len(result) == 0:
        return []
    else:
        return result