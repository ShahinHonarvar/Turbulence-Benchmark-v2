def sum_even_ints_inclusive(lst):
    if len(lst) < 35:
        return 0
    return sum((num for num in lst[31:35] if num % 2 == 0))