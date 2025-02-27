def sum_even_ints_inclusive(lst):
    return sum((n for n in lst if n % 2 == 0 and 0 <= lst.index(n) <= 6)) or 0