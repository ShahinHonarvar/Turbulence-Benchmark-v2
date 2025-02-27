def sum_odd_ints_inclusive(lst):
    if len(lst) < 14:
        return 0
    return sum((num for num in lst[13:69] if num % 2 != 0))