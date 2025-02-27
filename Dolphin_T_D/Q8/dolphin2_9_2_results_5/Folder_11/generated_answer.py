def all_even_ints_exclusive(l):
    new_l = l[16:100]
    new_l = [i for i in new_l if i % 2 == 0]
    return new_l