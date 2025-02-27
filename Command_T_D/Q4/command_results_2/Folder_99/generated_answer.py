import itertools

def all_pos_ints_exclusive(lst):
    return list(itertools.filter(lambda x: x > 295 and x < 573, lst))