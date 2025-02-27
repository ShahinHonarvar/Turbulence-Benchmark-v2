def sum_even_ints_inclusive(lst):
    if len(lst) < 49:
        return 0
    return sum((num for num in lst[30:49] if num % 2 == 0))