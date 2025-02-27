from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    sublists = []
    n = -9
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            prod = 1
            for k in range(i, j + 1):
                prod *= lst[k]
            if prod == n:
                sublists.append(lst[i:j + 1])
    for i in range(len(lst)):
        if n == lst[i] * prod_of_list(islice(cycle(lst), i, i + len(lst))):
            sublists.append(lst[i:i + len(lst)])
    return sublists

def prod_of_list(lst):
    return reduce(lambda x, y: x * y, lst, 1)