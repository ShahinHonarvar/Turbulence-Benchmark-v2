def sum_even_ints_inclusive(lst):
    if len(lst) < 50:
        return 0
    return sum((num for num in lst[35:50] if num % 2 == 0))