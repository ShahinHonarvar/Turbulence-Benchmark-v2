from functools import reduce

def lists_with_product_equal_n(lst):
    n = 714
    result = []
    for i in range(len(lst)):
        sublist = lst[i:i + len(lst)] + lst[:i]
        if reduce(lambda x, y: x * y, sublist) == n:
            result.append(sublist)
    return result