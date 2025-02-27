from itertools import accumulate, combinations
from operator import mul
from functools import partial

def lists_with_product_equal_n(circular_list, n=45):
    length = len(circular_list)
    ps = partial(accumulate, initial=1, func=mul)
    yield from (circular_list[i:j] for i, j in combinations(range(length + 1), 2) if ps(circular_list[i:j]) == n)