def all_odd_ints_exclusive(lst):
    if not any((x % 2 for x in lst[80:200])):
        return []
    return [x for x in lst[80:200] if x % 2]