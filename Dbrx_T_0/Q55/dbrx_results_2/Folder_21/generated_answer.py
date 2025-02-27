from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    n = 851
    result = []
    for i in range(len(lst)):
        sublst = [lst[i]]
        for j in range(i + 1, len(lst)):
            sublst.append(lst[j])
            if sublst[-1] == 0:
                break
            if prod(sublst) == n:
                result.append(sublst)
                break
            if prod(sublst) > n:
                break
    return result

def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p