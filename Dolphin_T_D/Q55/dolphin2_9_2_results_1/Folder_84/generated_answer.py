from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    n = -906
    sublist = []
    products = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == n:
                sublist.append(list(islice(cycle(lst), i, j + 1)))
    return sublist