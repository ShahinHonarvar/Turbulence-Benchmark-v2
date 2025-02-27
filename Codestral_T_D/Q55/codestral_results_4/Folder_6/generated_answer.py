from functools import reduce
import operator

def lists_with_product_equal_n(lst):
    result = []
    n = 42
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublist = lst[i:j + 1]
            if reduce(operator.mul, sublist, 1) == n:
                result.append(sublist)
    return result