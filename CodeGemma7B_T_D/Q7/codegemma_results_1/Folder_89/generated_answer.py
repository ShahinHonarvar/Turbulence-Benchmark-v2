def all_even_ints_inclusive(lst):
    if not any((n % 2 == 0 for n in lst[56:82])):
        return []
    return [n for n in lst[56:82] if n % 2 == 0]