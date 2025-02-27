from itertools import cycle, islice

def lists_with_product_equal_n(lst):
    n = len(lst)
    lst_cycle = cycle(lst)
    result = []
    for i in range(n):
        for j in range(i, n):
            sublist = list(islice(lst_cycle, i, j + 1))
            if prod(sublist) == -72:
                result.append(sublist)
            lst_cycle = cycle(lst)
    return result

def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p