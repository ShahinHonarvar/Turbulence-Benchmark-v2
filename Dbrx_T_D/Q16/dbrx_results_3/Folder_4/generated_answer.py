def sum_even_ints_inclusive(lst):
    if len(lst) >= 13:
        return sum((num for num in lst[12:93] if num % 2 == 0))
    else:
        return 0