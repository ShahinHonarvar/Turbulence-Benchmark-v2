def sum_odd_ints_inclusive(lst):
    if not 4 <= 8 < len(lst):
        return 0
    else:
        return sum((i for i in lst[4:9] if i % 2 != 0))