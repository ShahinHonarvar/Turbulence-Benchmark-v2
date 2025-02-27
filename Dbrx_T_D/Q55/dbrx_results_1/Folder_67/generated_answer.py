from itertools import islice

def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for j in range(1, len(lst) - i + 1):
            sublist = list(islice(circular(lst, i), j))
            if prod(sublist) == 33:
                result.append(sublist)
    return result

def circular(lst, idx):
    return (lst[i] for i in range(idx, len(lst) + idx))

def prod(lst):
    if not lst:
        return 1
    else:
        accumulation = 1
        for i in lst:
            accumulation *= i
        return accumulation