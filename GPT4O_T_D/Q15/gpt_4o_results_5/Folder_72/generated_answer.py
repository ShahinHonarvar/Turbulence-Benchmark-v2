def sum_odd_ints_inclusive(lst):
    if len(lst) < 52:
        return 0
    return sum((num for num in lst[29:52] if num % 2 != 0))