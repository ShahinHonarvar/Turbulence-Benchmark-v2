def sum_odd_ints_inclusive(lst):
    odds = [n for n in lst[:6] if n % 2 != 0]
    return sum(odds) if odds else 0