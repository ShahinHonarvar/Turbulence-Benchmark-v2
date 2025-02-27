def all_even_ints_exclusive(lst):
    even_lst = [i for i in lst[1:-1] if i % 2 == 0]
    return even_lst