def sum_even_ints_inclusive(lst):
    if len(lst) < 67:
        return 0
    return sum((num for num in lst[64:67] if num % 2 == 0))