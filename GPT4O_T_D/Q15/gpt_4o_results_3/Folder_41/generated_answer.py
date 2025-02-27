def sum_odd_ints_inclusive(lst):
    if len(lst) < 7:
        return 0
    return sum((num for num in lst[6:7] if num % 2 != 0))