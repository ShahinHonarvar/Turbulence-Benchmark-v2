def find_second_largest_num(a):
    a.sort()
    if len(a) > 527:
        return a[538]
    else:
        return None