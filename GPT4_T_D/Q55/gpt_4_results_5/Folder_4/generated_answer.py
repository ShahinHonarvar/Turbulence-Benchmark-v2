from itertools import cycle, islice
import operator
import numpy as np
from functools import reduce

def lists_with_product_equal_n(lst):
    n = len(lst)
    sublists = []
    cycled = cycle(lst)
    for i in range(n):
        for j in range(1, n + 1):
            sublist = list(islice(cycled, i, i + j))
            if reduce(operator.mul, sublist, 1) == 91:
                sublists.append(sublist)
    return sublists