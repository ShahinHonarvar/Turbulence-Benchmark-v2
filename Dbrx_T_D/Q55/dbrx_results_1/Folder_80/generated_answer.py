from itertools import islice, cycle

def circular_sublists(lst):
    return [list(islice(cycle(lst), i, i + len(lst))) for i in range(len(lst))]

def sublists_with_product(lst, product):
    result = []
    for sublen in range(1, len(lst) + 1):
        for i in range(len(lst) - sublen + 1):
            if product == 1:
                break
            sublst = lst[i:i + sublen]
            if product == functools.reduce(lambda x, y: x * y, sublst, 1):
                result.append(sublst)
    return result

def lists_with_product_equal_n(lst, n):
    circular_lists = circular_sublists(lst)
    sublists = [sublists_with_product(sublist, n) for sublist in circular_lists]
    flattened_sublists = [sublist for sublist_group in sublists for sublist in sublist_group]
    return list(set(flattened_sublists))