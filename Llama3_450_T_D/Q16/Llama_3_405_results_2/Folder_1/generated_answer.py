def sum_even_ints_inclusive(lst):
    return sum([num for i, num in enumerate(lst) if i >= 31 and i <= 72 and (num % 2 == 0)])