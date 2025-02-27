def sum_even_ints_inclusive(lst):
    if len(lst) < 5:
        return 0
    num = lst[4]
    return num if num % 2 == 0 else 0