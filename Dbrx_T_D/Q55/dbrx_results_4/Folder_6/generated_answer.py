from itertools import islice

def circular_list_slice(lst, start, end):
    result = lst[start:end]
    if end < start:
        result += lst[:end]
    return result

def all_sublists(lst):
    n = len(lst)
    return [circular_list_slice(lst, i, i + n) for i in range(n)]

def product(lst):
    return reduce(lambda x, y: x * y, lst, 1)

def lists_with_product_equal_n(lst):
    n = 42
    all_sublists_in_order = all_sublists(lst)
    matching_sublists = filter(lambda sublist: product(sublist) == n, all_sublists_in_order)
    return list(matching_sublists)