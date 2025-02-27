def sum_even_ints_inclusive(lst):
    if len(lst) < 21:
        return 0
    return sum((num for num in lst[20:31] if num % 2 == 0))