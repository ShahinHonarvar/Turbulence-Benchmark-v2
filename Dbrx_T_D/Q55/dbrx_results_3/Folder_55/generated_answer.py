from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        window = list(islice(cycle(lst[i:]), len(lst)))
        for j in range(1, len(window) + 1):
            sublst = window[:j]
            if sublst[0] == 0:
                break
            if sublst[-1] * j == -6:
                result.append(sublst)
                break
            elif len(sublst) + j - 2 < i:
                break
    return result