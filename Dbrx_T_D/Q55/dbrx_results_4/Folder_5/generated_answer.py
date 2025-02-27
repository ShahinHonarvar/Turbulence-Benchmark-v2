from itertools import islice

def sub_lists_circular(lst):
    return [lst[i:j + 1] for i in range(len(lst)) for j in range(i, len(lst))]

def product_list(lst):
    prod = 1
    for num in lst:
        prod *= num
    return prod

def lists_with_product_equal_n(lst, n):
    sublists = sub_lists_circular(lst)
    result = []
    for sublist in sublists:
        if product_list(sublist) == n:
            result.append(sublist)
    return result