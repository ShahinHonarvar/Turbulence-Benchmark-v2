from itertools import islice, chain

def lists_with_product_equal_n(lst):
    n = -82
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublst = list(islice(chain(lst[j:], lst[:j]), i, j + 1))
            if sublst and sublst[-1] != 0 and ((-1) ** len(sublst) * reduce(lambda x, y: x * y, sublst, 1) == n):
                result.append(sublst)
    return result