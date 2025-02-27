def sum_even_ints_inclusive(lst):
    if len(lst) < 99:
        return 0
    return sum((num for num in lst[56:99] if num % 2 == 0))