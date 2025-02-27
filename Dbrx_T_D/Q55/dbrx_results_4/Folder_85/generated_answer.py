from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    n = -97
    result = []
    circular_lst = list(lst)
    for i in range(len(circular_lst)):
        for j in range(i, len(circular_lst)):
            sublst = list(islice(cyclic_sublst(circular_lst, i), j - i + 1))
            if produce(sublst) == n:
                result.append(sublst)
    return result

def cyclic_sublst(lst, start):
    for i in cycle(lst):
        yield i
        start = (start + 1) % len(lst)

def produce(lst):
    p = 1
    for i in lst:
        p *= i
    return p