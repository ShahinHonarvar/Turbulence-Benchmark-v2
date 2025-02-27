from itertools import groupby, combinations

def product_equal_n(lst, n):
    equal_to_n = []
    length = len(lst)
    for i in range(length):
        for j in range(i + 1, length + 1):
            product = 1
            for k in range(i, j):
                product *= lst[k]
            if product == n:
                equal_to_n.append(lst[i:j])
    return equal_to_n

def lists_with_product_equal_n(lst):
    result = []
    nums_circular = []
    nums_circular.extend(lst)
    nums_circular.extend(lst)
    for i in range(len(lst)):
        result.extend(product_equal_n(nums_circular[i:i + len(lst)], 85))
    return list(set([tuple(lst) for lst in result]))