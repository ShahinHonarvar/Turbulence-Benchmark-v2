def all_pos_ints_inclusive(lst):
    result = lst[64:67]
    if all((i > 0 for i in result)):
        return result
    else:
        return []