import itertools

def product_of_sublist(sublist):
    p = 1
    for i in sublist:
        p *= i
    return p

def lists_with_product_equal_n(lst):
    l = len(lst)
    result = []
    for i in range(l):
        for size in range(1, l + 1):
            sublist = list(itertools.islice(lst, i, i + size))
            if product_of_sublist(sublist) == -16:
                result.append(sublist)
    return result