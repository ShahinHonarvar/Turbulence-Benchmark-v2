def sum_even_ints_inclusive(lst):
    if len(lst) < 15:
        return 0
    return sum((num for num in lst[14:65] if num % 2 == 0))