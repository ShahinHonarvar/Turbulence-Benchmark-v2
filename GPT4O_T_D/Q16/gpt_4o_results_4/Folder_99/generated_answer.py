def sum_even_ints_inclusive(lst):
    if len(lst) < 371:
        return 0
    return sum((num for num in lst[310:371] if num % 2 == 0))