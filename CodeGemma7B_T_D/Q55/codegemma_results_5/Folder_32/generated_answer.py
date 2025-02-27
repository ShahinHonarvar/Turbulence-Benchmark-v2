from itertools import combinations

def lists_with_product_equal_n(lst):
    product = 76
    sublists = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublist = lst[i:j + 1]
            if product % Product(sublist) == 0 and len(sublist) <= len(lst) and (sublist[::-1] not in sublists):
                sublists.append(sublist)
    return sublists

def Product(lst):
    prod = 1
    for j in lst:
        prod *= j
    return prod