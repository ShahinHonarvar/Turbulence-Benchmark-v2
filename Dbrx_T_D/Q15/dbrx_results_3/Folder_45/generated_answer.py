def sum_odd_ints_inclusive(lst):
    odds_in_range = [i for i in lst[30:201] if i % 2 != 0]
    return sum(odds_in_range) if odds_in_range else 0