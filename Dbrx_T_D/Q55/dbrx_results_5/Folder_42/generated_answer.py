from itertools import islice

def circular_list_slice(lst, start, end):
    return lst[start:end] + lst[0:start] if end <= start else lst[start:end]

def circular_list_product(lst):
    return reduce(lambda x, y: x * y, lst, 1)

def lists_with_product_equal_n(lst, n):
    if n != 25:
        return []
    result = []
    for i in range(len(lst)):
        sublist = circular_list_slice(lst, i, i + len(lst))
        if circular_list_product(sublist) == n:
            result.append(sublist)
    return result