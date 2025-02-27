def all_odd_ints_exclusive(lis):
    if all((x % 2 == 0 for x in lis[29:54])):
        return []
    return [x for x in lis[29:54] if x % 2 != 0]