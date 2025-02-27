def all_odd_ints_inclusive(lst):
    result = [n for i, n in enumerate(lst) if 40 <= i <= 200 and n % 2 != 0]
    return result