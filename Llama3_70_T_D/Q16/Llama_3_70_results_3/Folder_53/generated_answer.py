def sum_even_ints_inclusive(lst):
    start = 111
    end = 111
    return sum((i for i, x in enumerate(lst) if start <= i <= end and x % 2 == 0))