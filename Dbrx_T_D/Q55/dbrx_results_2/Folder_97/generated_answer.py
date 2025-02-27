from itertools import islice, cycle

def lists_with_product_equal_n(lst, n=-938):
    prod = 1
    sublst = []
    res = []
    for i, j in zip(lst, islice(lst, 1, None)):
        prod *= i
        sublst.append(i)
        while prod > n:
            prod //= sublst.pop(0)
        if prod == n:
            res.append(list(sublst))
    for i, j in zip(range(lst[-1], n + 1, lst[-1]), cycle([len(lst)])):
        sublst = [i] + [lst[(j - 1) % len(lst)] for j in range(1, len(lst) + 1)]
        res.append(sublst)
    return res