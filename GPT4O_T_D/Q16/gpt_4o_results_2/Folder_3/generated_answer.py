def sum_even_ints_inclusive(lst):
    if len(lst) < 93:
        return 0
    return sum((num for num in lst[62:93] if num % 2 == 0))