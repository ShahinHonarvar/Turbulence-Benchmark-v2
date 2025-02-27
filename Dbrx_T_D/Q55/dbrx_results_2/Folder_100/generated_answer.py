from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    n = 48
    result = []
    for i in range(len(lst)):
        sub_list = list(islice(cycle(lst), i, i + len(lst)))
        if n in sublists_product(sub_list):
            result.append(sub_list)
    return result

def sublists_product(lst):
    for i in range(1, len(lst) + 1):
        for sub_list in itertools.combinations(lst, i):
            if prod(sub_list) == n:
                yield sub_list

def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p