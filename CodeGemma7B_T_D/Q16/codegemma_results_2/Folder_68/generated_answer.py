def sum_even_ints_inclusive(lst):
    if not any((num % 2 == 0 for num in lst[0:9])):
        return 0
    return sum((num for num in lst[0:9] if num % 2 == 0))