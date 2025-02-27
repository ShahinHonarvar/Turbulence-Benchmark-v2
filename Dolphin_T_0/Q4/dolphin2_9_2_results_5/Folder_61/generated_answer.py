def all_pos_ints_exclusive(lst):
    result = []
    for n in lst[1:-1]:
        if n > 0:
            result.append(n)
    return result