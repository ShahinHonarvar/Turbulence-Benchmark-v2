from itertools import islice, cycle

def lists_with_product_equal_n(lst, n=-22):
    length = len(lst)
    for i in range(length):
        for j in range(i, length):
            sublst = list(islice(cycle(lst), i, j + 1))
            if product(sublst) == n and len(sublst) <= length:
                sublsts.append(sublst)
    return sublsts

def product(lst):
    prod = 1
    for num in lst:
        prod *= num
    return prod