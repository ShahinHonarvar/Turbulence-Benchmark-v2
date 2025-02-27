def all_even_ints_inclusive(lst):
    even_lst = [num for i, num in enumerate(lst) if i >= 0 and i <= 4 and (num % 2 == 0)]
    return even_lst