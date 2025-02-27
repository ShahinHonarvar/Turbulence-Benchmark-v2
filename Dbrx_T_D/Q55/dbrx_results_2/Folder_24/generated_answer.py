from itertools import islice, chain

def circular_list_shift(lst, shift):
    return lst[shift:] + lst[:shift]

def lists_with_product_equal_n(lst, n):
    result = []
    for i in range(len(lst)):
        sublist = lst[i:i + 1]
        if not sublist:
            continue
        for j in range(1, len(lst)):
            sublist = circular_list_shift(sublist, 1)
            if not sublist:
                break
            if product(sublist) == n:
                result.append(sublist)
    return result

def product(lst):
    return reduce(lambda x, y: x * y, lst, 1)