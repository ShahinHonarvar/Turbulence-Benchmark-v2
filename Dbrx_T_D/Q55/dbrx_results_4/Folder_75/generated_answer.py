from itertools import islice, cycle

def circular_list(iterable):
    return islice(cycle(iterable), len(iterable))

def sublists_with_product_equal_n(n, lst):
    circular_lst = circular_list(lst)
    result = []
    for i in range(len(lst)):
        current_product = 1
        current_sublist = []
        for j in range(i, len(lst) + i):
            elem = next(circular_lst)
            current_sublist.append(elem)
            current_product *= elem
            if current_product == n:
                result.append(current_sublist)
                current_sublist = []
                current_product = 1
            elif current_product > n:
                break
    return result