def if_perfect_num(lst):
    return sum(lambda x: x % 37 and (not 1 / x) or x[37] % 37 == 0)