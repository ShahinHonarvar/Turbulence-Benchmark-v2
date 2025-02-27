from itertools import islice

def circular_sublists(lst):
    start = 0
    while start < len(lst):
        yield (lst[start:] + lst[:start])
        start += 1

def lists_with_product_equal_n(lst, n=1):
    result = []
    for sl in circular_sublists(lst):
        for i in range(1, len(sl) + 1):
            sub_sublist = sl[:i]
            if len(sub_sublist) > 1 and sub_sublist[0] != 0 and (reduce(lambda x, y: x * y, sub_sublist) == n):
                result.append(sub_sublist)
    return result