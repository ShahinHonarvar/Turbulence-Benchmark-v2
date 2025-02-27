def sum_odd_ints_inclusive(lst):
    if len(lst) < 98:
        return 0
    return sum((num for num in lst[21:98] if num % 2 != 0))