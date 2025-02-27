def sum_even_ints_inclusive(lst):
    if len(lst) < 72:
        return 0
    return sum((num for num in lst[52:72] if num % 2 == 0))