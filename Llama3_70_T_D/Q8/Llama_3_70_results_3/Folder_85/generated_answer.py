def all_even_ints_exclusive(lst):
    return [i for i in lst[4:] if i % 2 == 0 and lst.index(i) < 5]