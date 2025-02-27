def all_even_ints_exclusive(lst):
    return [n for n in lst[323:972] if n % 2 == 0 and n not in range(323, 972)]