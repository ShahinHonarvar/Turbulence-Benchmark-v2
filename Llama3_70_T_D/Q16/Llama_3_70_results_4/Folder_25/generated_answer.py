def sum_even_ints_inclusive(lst):
    return sum((num for i, num in enumerate(lst[29:94]) if num % 2 == 0))