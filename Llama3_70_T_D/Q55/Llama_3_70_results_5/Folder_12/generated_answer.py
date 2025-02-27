def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for size in range(1, n + 1):
        for i in range(n):
            sublst = lst[i:i + size]
            if len(sublst) < size:
                sublst += lst[:size - len(sublst)]
            if 0 not in sublst and -18 ** len(sublst) % 2 == -18 % 2 and (-18 ** len(sublst) % abs(sublst[0]) == -18 % abs(sublst[0])) and (eval('*'.join(map(str, sublst))) == -18):
                result.append(sublst)
    return result