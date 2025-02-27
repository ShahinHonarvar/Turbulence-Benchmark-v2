def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(1, n + 1):
            sublist = lst[i:i + j]
            if len(sublist) < n and 0 not in sublist and (eval('*'.join(map(str, sublist))) == 25):
                result.append(sublist)
    return result