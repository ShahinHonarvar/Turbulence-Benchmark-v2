def sum_even_ints_inclusive(lst):
    return sum((num for i, num in enumerate(lst[60:201], 60) if num % 2 == 0))