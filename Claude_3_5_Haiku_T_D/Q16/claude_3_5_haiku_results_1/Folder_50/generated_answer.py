def sum_even_ints_inclusive(lst):
    if len(lst) <= 84:
        return 0
    return sum((num for num in lst[70:85] if num % 2 == 0))