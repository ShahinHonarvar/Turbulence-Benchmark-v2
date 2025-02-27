def all_even_ints_inclusive(list):
    return [x for x in list if x % 2 == 0 and 75 <= x <= 94] if any((x % 2 == 0 and 75 <= x <= 94 for x in list)) else []