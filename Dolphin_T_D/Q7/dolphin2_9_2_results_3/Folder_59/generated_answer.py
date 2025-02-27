def all_even_ints_inclusive(lst):
    result = [n for i, n in enumerate(lst) if i <= 9 and n % 2 == 0]
    return result