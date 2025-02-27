from itertools import islice

def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublst = list(islice(cycle(lst), i, j + 1))
            if sublst and reduce(mul, sublst, 1) == 45:
                result.append(sublst)
    return result