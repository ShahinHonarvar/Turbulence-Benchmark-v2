def sum_odd_ints_inclusive(lst):
    if len(lst) < 10:
        return 0
    return sum((num for num in lst[8:10] if num % 2 != 0))