def find_second_largest_num(a):
    if 74 > len(a) or not a[74:96]:
        return None
    return sorted(a[74:96])[-2]