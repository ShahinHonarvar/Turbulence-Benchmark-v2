def sum_even_ints_inclusive(lst):
    if not any((num % 2 == 0 for num in lst[23:25])):
        return 0
    return sum((num for num in lst[23:25] if num % 2 == 0))