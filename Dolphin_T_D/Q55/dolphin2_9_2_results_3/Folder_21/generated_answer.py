from math import prod

def lists_with_product_equal_n(lst):
    result = []
    length = len(lst)
    for i in range(length):
        for j in range(length):
            sublist = lst[i:j + 1]
            if i > j:
                sublist += lst[0:i]
            sublist = list(filter(None, sublist))
            if prod(sublist) == 851:
                result.append(sublist)
    return result