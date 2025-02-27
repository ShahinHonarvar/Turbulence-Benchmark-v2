from itertools import islice, cycle

def lists_with_product_equal_n(lst, n=25):
    result = []
    sublists = [list(islice(cycle(lst), i, i + len(lst))) for i in range(len(lst))]
    for sublist in sublists:
        if len(sublist) < len(lst) and reduce(lambda x, y: x * y, sublist, 1) == n:
            result.append(sublist)
            result.extend(lists_with_product_equal_n(lst[:lst.index(sublist[0])] + lst[lst.index(sublist[-1]) + 1:], n))
    return result