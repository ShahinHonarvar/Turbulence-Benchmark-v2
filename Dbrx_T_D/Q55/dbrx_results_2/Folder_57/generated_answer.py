from itertools import islice

def circular_list_slice(clist, start, end):
    return clist[start:end] + clist[:end - len(clist) + start] if end > start else clist[start:end]

def lists_with_product_equal_n(clist, n):
    result = []
    for i in range(len(clist)):
        for j in range(i, len(clist)):
            sublist = circular_list_slice(clist, i, j + 1)
            if reduce(lambda x, y: x * y, sublist) == n:
                result.append(sublist)
    return result