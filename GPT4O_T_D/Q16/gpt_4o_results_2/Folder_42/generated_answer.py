def sum_even_ints_inclusive(lst):
    if len(lst) < 30:
        return 0
    return sum((num for num in lst[29:80] if num % 2 == 0))