from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        window = list(islice(cycle(lst[i:]), len(lst)))
        for j in range(1, len(window) + 1):
            sublst = window[:j]
            if sublst[0] * sublst[-1] == -18:
                result.append(sublst)
    return result