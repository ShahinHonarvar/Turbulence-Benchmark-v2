from itertools import islice, cycle

def circular_sublists(lst):
    return [list(islice(cycle(lst), i, i + len(lst))) for i in range(len(lst))]

def lists_with_product_equal_n(lst, n):
    circular_sublists_of_lst = circular_sublists(lst)
    result = [sublist for sublist in circular_sublists_of_lst if sublists_product(sublist) == n]
    return result

def sublists_product(sublist):
    return prod(sublist)

def prod(lst):
    if not lst:
        return 1
    else:
        return lst[0] * prod(lst[1:])