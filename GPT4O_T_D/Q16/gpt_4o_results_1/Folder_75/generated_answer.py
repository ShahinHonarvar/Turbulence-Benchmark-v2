def sum_even_ints_inclusive(lst):
    if len(lst) < 58:
        return 0
    return sum((num for num in lst[56:58 + 1] if num % 2 == 0))