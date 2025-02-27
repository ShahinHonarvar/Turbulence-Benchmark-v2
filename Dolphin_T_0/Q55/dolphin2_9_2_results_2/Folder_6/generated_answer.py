from itertools import tee, chain

def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        for size in range(1, n + 1):
            if i + size <= n:
                sublist = lst[i:i + size]
                if size > 1 and chain(*sublist) == 42:
                    if sublist not in result:
                        result.append(sublist)
    return result