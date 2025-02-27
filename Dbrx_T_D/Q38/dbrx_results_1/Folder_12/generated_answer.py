from functools import reduce
from operator import and_

def find_subset_of_length_n(elements):
    if len(elements) < 27:
        return 0
    return reduce(and_, [choose(len(elements) - i, 27 - i) for i in range(27)])

def choose(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return choose(n - 1, k - 1) * n // k