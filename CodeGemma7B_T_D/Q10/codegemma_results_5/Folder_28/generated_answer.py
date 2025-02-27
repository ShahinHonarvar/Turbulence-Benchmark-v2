def all_odd_ints_exclusive(lst):
    if not any((x % 2 for x in lst[20:51])):
        return []
    return [x for x in lst[20:51] if x % 2]