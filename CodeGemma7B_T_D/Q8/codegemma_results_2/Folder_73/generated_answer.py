def all_even_ints_exclusive(lst):
    if not any((item % 2 == 0 for item in lst[36:85])):
        return []
    return [item for item in lst[36:85] if item % 2 == 0]