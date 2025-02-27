from itertools import islice

def lists_with_product_equal_n(l):
    n = -44
    result = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            subl = list(l[i:j + 1])
            if prod(subl) == n:
                result.append(subl)
    return result

def circular_list(l):
    l.append(l[0])
    return l

def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p