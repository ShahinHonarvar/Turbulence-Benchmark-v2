def sum_odd_ints_inclusive(lst):
    odds = [i for i in lst[667:775] if i % 2 != 0]
    return sum(odds) if odds else 0