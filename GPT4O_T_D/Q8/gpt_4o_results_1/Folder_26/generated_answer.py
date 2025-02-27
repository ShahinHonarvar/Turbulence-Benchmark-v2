def all_even_ints_exclusive(lst):
    if len(lst) <= 45:
        return []
    return [n for n in lst[45:78] if n % 2 == 0]