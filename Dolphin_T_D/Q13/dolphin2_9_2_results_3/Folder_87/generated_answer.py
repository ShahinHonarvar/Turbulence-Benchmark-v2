def find_second_largest_num(l):
    if len(l) < 2:
        return None
    li = l[35:47]
    return sorted(list(set(li)))[1] if len(set(li)) >= 2 else None