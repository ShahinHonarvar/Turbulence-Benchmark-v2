def all_even_ints_exclusive(lst):
    even_ints = [i for i in lst[1:-1] if i % 2 == 0]
    return even_ints