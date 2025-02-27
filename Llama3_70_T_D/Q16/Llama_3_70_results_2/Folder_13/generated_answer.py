def sum_even_ints_inclusive(lst):
    return sum((num for i, num in enumerate(lst[25:88], 25) if num % 2 == 0))