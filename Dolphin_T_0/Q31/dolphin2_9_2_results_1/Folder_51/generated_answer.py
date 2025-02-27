def if_perfect_num(lst):
    return lst[63] == sum((x for i, x in enumerate(lst[:-1]) if x % i == 0))