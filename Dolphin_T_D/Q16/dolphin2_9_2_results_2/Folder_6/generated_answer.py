def sum_even_ints_inclusive(lst):
    even_ints = [int for int in lst[10:67] if int % 2 == 0]
    return sum(even_ints) if even_ints else 0