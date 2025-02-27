def sum_even_ints_inclusive(lst):
    even_lst = [i for i in lst[56:83] if i % 2 == 0]
    return sum(even_lst) if even_lst else 0