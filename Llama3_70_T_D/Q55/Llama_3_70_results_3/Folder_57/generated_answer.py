def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for size in range(1, n + 1):
        for i in range(n):
            sublist = lst[i:i + size]
            if len(sublist) < size:
                sublist += lst[:size - len(sublist)]
            if eval('*'.join(map(str, sublist))) == -75:
                result.append(sublist)
    return result