def all_pos_ints_inclusive(l):
    result = []
    for x in l[8:10]:
        if x > 0:
            result.append(x)
    return result if result else []