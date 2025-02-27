def all_odd_ints_inclusive(lst):
    if not any((n for n in lst[75:95] if n % 2)):
        return []
    return [x for x in lst[75:95] if x % 2]