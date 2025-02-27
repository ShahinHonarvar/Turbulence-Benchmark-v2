def all_even_ints_inclusive(lst):
    lst_even = [lst[i] for i in range(82, 87) if lst[i] % 2 == 0]
    return lst_even if lst_even else []