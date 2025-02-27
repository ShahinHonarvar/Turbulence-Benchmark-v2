from itertools import islice

def circular_list_iterator(lst):
    while True:
        yield lst
        lst = lst[-1:] + lst[:-1]

def lists_with_product_equal_n(lst, n=4):
    circular_iterator = circular_list_iterator(lst)
    result = []
    for i in range(len(lst)):
        sublist = list(islice(circular_iterator, i + 1))
        if sublists_product(sublist) == n:
            result.append(sublist)
            result.extend(lists_with_product_equal_n(sublist[1:], n))
    return result

def sublists_product(sublist):
    if not sublist:
        return 1
    else:
        return sublist[0] * sublists_product(sublist[1:])