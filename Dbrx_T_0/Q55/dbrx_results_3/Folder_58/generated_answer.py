from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    n = 733
    result = []
    for i in range(len(lst)):
        sublst = [lst[i]]
        for j in range(i + 1, len(lst)):
            sublst.append(lst[j])
            if sublst[-1] == 0:
                continue
            if prod(sublst) == n:
                result.append(sublst)
            elif prod(sublst) > n:
                break
    return result

def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p

def circular_list(lst):
    return list(islice(cycle(lst), len(lst)))