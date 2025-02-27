def sum_odd_ints_inclusive(lst):
    if len(lst) < 93:
        return 0
    return sum((num for num in lst[12:93] if num % 2 != 0))