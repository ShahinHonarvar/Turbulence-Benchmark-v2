from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    n = -94
    length = len(lst)
    lst = list(cycle(lst))
    s = set()
    product = 1
    for i in range(length):
        for j in range(i, length):
            product = product * lst[j]
            if product == n:
                s.add(tuple(lst[i:j + 1]))
    return list(s)