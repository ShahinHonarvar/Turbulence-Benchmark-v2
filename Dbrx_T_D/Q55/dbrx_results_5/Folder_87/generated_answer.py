from itertools import islice

def circular_list_iterator(lst):
    while True:
        for i in lst:
            yield i

def product(lst):
    result = 1
    for i in lst:
        result *= i
    return result

def lists_with_product_equal_n(lst, n):
    result = []
    lst_it = circular_list_iterator(lst)
    for i in range(len(lst)):
        sublst = list(islice(lst_it, i + 1))
        if product(sublst) == n:
            result.append(sublst)
    return result