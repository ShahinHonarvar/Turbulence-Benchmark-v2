def all_even_ints_exclusive(lst):
    even_lst = [x for x in lst[1:-1] if x % 2 == 0]
    return even_lst