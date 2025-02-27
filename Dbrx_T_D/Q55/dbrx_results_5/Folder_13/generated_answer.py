from itertools import islice

def circular_list(lst):
    return lst + [lst[0]]

def lists_with_product_equal_n(lst, n=54):
    result = []
    for i in range(len(lst)):
        sublist = list(islice(circular_list(lst[i:]), i + 1))
        if sublist and n in (sublist[0], *[sublist[0] * x for x in sublist[1:]]):
            result.append(sublist)
    return result