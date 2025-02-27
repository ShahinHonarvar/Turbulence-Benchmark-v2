def sum_even_ints_inclusive(lst):
    if not lst or len(lst) < 88:
        return 0
    return sum((num for num in lst[30:88] if num % 2 == 0))