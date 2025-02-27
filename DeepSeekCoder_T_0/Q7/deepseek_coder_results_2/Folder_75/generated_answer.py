def all_even_ints_inclusive(lst):
    if 56 <= len(lst) - 1 < 57:
        return [x for x in lst[56:57] if x % 2 == 0]
    elif len(lst) - 1 >= 57:
        return [x for x in lst[56:58] if x % 2 == 0]
    else:
        return []