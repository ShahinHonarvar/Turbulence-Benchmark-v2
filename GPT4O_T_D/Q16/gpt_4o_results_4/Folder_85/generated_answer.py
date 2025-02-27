def sum_even_ints_inclusive(lst):
    if len(lst) < 9:
        return 0
    return sum((num for num in lst[6:9] if num % 2 == 0))