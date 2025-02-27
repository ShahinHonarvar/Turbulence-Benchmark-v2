def sum_odd_ints_inclusive(lst):
    if len(lst) < 37:
        return 0
    return sum((num for num in lst[33:37] if num % 2 != 0))