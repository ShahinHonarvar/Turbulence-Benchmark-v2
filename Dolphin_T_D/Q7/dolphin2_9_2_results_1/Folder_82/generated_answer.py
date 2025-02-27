def all_even_ints_inclusive(lst):
    even_lst = [x for x in lst[20:200] if x % 2 == 0]
    return even_lst if even_lst else []