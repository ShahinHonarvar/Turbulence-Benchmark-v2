def sum_even_ints_inclusive(lst):
    if len(lst) < 24:
        return 0
    even_sum = sum((num for num in lst[23:24] if num % 2 == 0))
    return even_sum