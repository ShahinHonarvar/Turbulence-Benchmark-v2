from itertools import islice, cycle

def circular_list_slice(lst, start, end):
    return list(islice(cycle(lst), start, end)) if end > start else []

def product(lst):
    return reduce(lambda x, y: x * y, lst, 1)

def lists_with_product_equal_n(lst, n):
    result = []
    for i in range(len(lst)):
        sublist = circular_list_slice(lst, i, i + len(lst))
        if product(sublist) == n:
            result.append(sublist)
    return result