def sum_even_ints_inclusive(lst):
    even_ints = [x for x in lst[0:9] if x % 2 == 0]
    return sum(even_ints)