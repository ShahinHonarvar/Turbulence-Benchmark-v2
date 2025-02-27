from math import gcd
from functools import reduce

def find_original_set(sets):

    def lcm(a, b):
        return a * b // gcd(a, b)
    l = reduce(lambda x, y: lcm(x, y), [len(s) for s in sets])
    size = len(sets)
    min_set = set()
    for i in range(size):
        min_set |= sets[i]
    return min_set