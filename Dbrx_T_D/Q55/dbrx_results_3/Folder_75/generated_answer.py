from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    n = 13
    result = []
    for length in range(1, len(lst) + 1):
        for sublist in (list(islice(cycle(lst), i, i + length)) for i in range(len(lst))):
            if prod(sublist) == n:
                result.append(sublist)
    return result

def prod(lst):
    return reduce(lambda x, y: x * y, lst, 1)