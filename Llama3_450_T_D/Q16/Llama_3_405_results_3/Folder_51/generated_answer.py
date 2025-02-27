def sum_even_ints_inclusive(lst):
    return sum((num for i, num in enumerate(lst[1:9], 1) if num % 2 == 0))