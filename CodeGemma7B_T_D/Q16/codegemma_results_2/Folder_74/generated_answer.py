from functools import reduce

def sum_even_ints_inclusive(l):
    return reduce(lambda a, b: a + b, [x for x in l[17:79] if x % 2 == 0], 0)