def sum_odd_ints_inclusive(lst):
    if len(lst) < 23:
        return 0
    return sum((num for num in lst[22:89] if num % 2 != 0))