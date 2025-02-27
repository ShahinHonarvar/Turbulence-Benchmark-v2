def sum_even_ints_inclusive(lst):
    even_ints = [i for i in lst[62:64] if i % 2 == 0]
    return sum(even_ints) if even_ints else 0